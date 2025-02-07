# users/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_list, name='user_list'),  # Главная страница
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
]

