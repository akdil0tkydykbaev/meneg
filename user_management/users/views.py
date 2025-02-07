from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm
from django.db.models import Q


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
    # search_number = request.GET.get('number', '')
    # search_direction = request.GET.get('direction', '')

    # Filter users by connection status and deletion status
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

    # # Apply search filters
    # if search_name:
    #     connected_users = connected_users.filter(name__icontains=search_name)
    #     not_connected_users = not_connected_users.filter(name__icontains=search_name)
    #
    # if search_number:
    #     connected_users = connected_users.filter(number__icontains=search_number)
    #     not_connected_users = not_connected_users.filter(number__icontains=search_number)
    #
    # if search_direction:
    #     connected_users = connected_users.filter(direction__icontains=search_direction)
    #     not_connected_users = not_connected_users.filter(direction__icontains=search_direction)

    return render(request, 'users/user_list.html', {
        'connected_users': connected_users,
        'not_connected_users': not_connected_users,
        'deleted_users': deleted_users,

        # 'search_name': search_name,
        # 'search_number': search_number,
        # 'search_direction': search_direction,
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
    interviewed_users = User.objects.filter(interviewed=True)
    not_interviewed_users = User.objects.filter(interviewed=False)

    return render(request, 'users/interview_list.html', {
        'interviewed_users': interviewed_users,
        'not_interviewed_users': not_interviewed_users,
    })


def toggle_interview_status(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Переключаем статус собеседования
    user.interviewed = not user.interviewed
    user.save()

    return redirect('interview_list')