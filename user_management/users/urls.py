from . import views
from django.urls import path
from .views import UserDetailView,delete_user_permanent
from .views import invite_to_interview, backend_interviews, frontend_interviews,user_detail, assign_trainer_view




urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('assign_trainer/<int:user_id>/', views.assign_trainer_view, name='assign_trainer'),
    path('add/', views.add_user, name='add_user'),  # Страница добавления пользователя
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),  # Страница редактирования
    path('toggle_connection/<int:user_id>/', views.toggle_connection, name='toggle_connection'),  # Связать / вернуть
    path('interview/', views.interview_list, name='interview_list'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('restore_user/<int:user_id>/', views.restore_user, name='restore_user'),
    path('permanent_delete_user/<int:user_id>/', views.permanent_delete_user, name='permanent_delete_user'),
    path('interviews/', views.interview_list, name='interview_list'),
    path('interviews/toggle_status/<int:user_id>/', views.toggle_interview_status, name='toggle_interview_status'),
    path('users/', views.user_list, name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
    path('user/<int:pk>/invite_to_interview/', views.invite_to_interview, name='invite_to_interview'),
    path('user/<int:pk>/invite/', invite_to_interview, name='invite_to_interview'),
    path('interviews/backend/', backend_interviews, name='backend_interviews'),
    path('interviews/frontend/', frontend_interviews, name='frontend_interviews'),
    path('assign-trainer/<int:user_id>/', assign_trainer_view, name='assign_trainer'),
    path('delete-user/<int:user_id>/', delete_user_permanent, name='delete_user_permanent'),
    path('interviews/assign_date/<int:user_id>/', views.assign_interview_date, name='assign_interview_date'),
    path('interviews/assign_trainer/<int:user_id>/', views.assign_trainer_view, name='assign_trainer'),
    path('trainers/create/', views.create_trainer_view, name='create_trainer'),
    path('trainers/<int:trainer_id>/edit/', views.edit_trainer_view, name='edit_trainer'),
    path('trainers/<int:trainer_id>/delete/', views.delete_trainer_view, name='delete_trainer'),
    path('trainers/', views.trainer_list_view, name='trainer_list'),


]

