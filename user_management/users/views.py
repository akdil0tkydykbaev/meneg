from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Trainer
from .forms import UserForm
from django.db.models import Q
from django.views.generic import DetailView
from django.http import HttpResponse
from django.utils import timezone
from .forms import TrainerForm




def restore_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_deleted = False  # Restore user
    user.save()
    return redirect('user_list')

def permanent_delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()  # Permanently delete user from database
    return redirect('user_list')

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_deleted = True  # Mark user as deleted
    user.save()
    return redirect('user_list')

def toggle_connection(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.connected = not user.connected  # Toggle the connected status
    user.save()
    return redirect('user_list')

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/edit_user.html', {'form': form, 'user': user})

def user_list(request):
    search_query = request.GET.get('search', '')  # Получаем общий запрос
    connected_users = User.objects.filter(is_deleted=False, connected=True)
    not_connected_users = User.objects.filter(is_deleted=False, connected=False)
    deleted_users = User.objects.filter(is_deleted=True)


    if search_query:
        connected_users = connected_users.filter(
            Q(name__icontains=search_query) |
            Q(number__icontains=search_query) |
            Q(direction__icontains=search_query)
        )
        not_connected_users = not_connected_users.filter(
            Q(name__icontains=search_query) |
            Q(number__icontains=search_query) |
            Q(direction__icontains=search_query)
        )


    return render(request, 'users/user_list.html', {
        'connected_users': connected_users,
        'not_connected_users': not_connected_users,
        'deleted_users': deleted_users,
    })

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect after successful save
    else:
        form = UserForm()
    return render(request, 'users/add_user.html', {'form': form})


def interview_list(request):
    frontend_users = User.objects.filter(direction="Frontend")
    backend_users = User.objects.filter(direction="Backend")

    return render(request, 'users/interview_list.html', {
        'frontend_users': frontend_users,
        'backend_users': backend_users,
    })

def toggle_interview_status(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Переключаем статус собеседования
    user.interviewed = not user.interviewed
    user.save()

    return redirect('interview_list')


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        interview_time = request.POST.get('interview_time')
        if interview_time:
            user.interview_time = interview_time
            user.save()
            return redirect('user_list')  # Перенаправляем после сохранения
    return render(request, 'users/user_detail.html', {'user': user})


def invite_to_interview(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        interview_time = request.POST.get('interview_time')
        if interview_time:
            user.interview_time = timezone.datetime.strptime(interview_time, '%Y-%m-%dT%H:%M')
            user.save()
            return redirect('user_list')
        else:
            return redirect('user_list')

    return render(request, 'users/invite_to_interview.html', {'user': user})


def backend_interviews(request):
    # Фильтрация пользователей с направлением Backend и датой собеседования
    users = User.objects.filter(direction='Backend', interview_time__isnull=False)
    return render(request, 'users/backend_interviews.html', {'users': users})



def frontend_interviews(request):
    # Фильтрация пользователей с направлением Frontend и датой собеседования
    users = User.objects.filter(direction='Frontend', interview_time__isnull=False)
    return render(request, 'users/frontend_interviews.html', {'users': users})


def delete_user_permanent(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('interview_list')  # Или куда нужно перенаправить

def assign_interview_date(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        interview_date = request.POST.get("interview_date")
        if interview_date:
            user.interview_date = interview_date
            user.save()
            return redirect('interview_list')  # Перенаправление обратно на страницу собеседования

    return HttpResponse("Invalid request", status=400)



def assign_trainer_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    trainers = Trainer.objects.all()

    if request.method == "POST":
        trainer_id = request.POST.get("trainer")
        trainer = get_object_or_404(Trainer, id=trainer_id)

        # Назначаем тренера
        user.trainer = trainer
        user.save()

        return redirect('interview_list')  # Возвращаемся на страницу собеседований

    return render(request, 'users/assign_trainer.html', {'user': user, 'trainers': trainers})

def delete_trainer_view(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    trainer.delete()
    return redirect('trainer_list')


def create_trainer_view(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')  # Перенаправляем на страницу со списком тренеров
    else:
        form = TrainerForm()

    return render(request, 'users/create_trainer.html', {'form': form})


def edit_trainer_view(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)

    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')  # Перенаправляем на страницу со списком тренеров
    else:
        form = TrainerForm(instance=trainer)

    return render(request, 'users/edit_trainer.html', {'form': form, 'trainer': trainer})

def trainer_list_view(request):
    trainers = Trainer.objects.all()
    return render(request, 'users/trainer_list.html', {'trainers': trainers})



