from . import views
from django.urls import path, include
from .views import CustomPasswordResetView
from django.contrib.auth import views as auth_views


#app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile_own, name='profile'),
    path('profile/<int:user_id>/', views.profile_user, name='profile_user'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit_profile, name='edit_profile'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('custom_password_reset/', auth_views.PasswordResetView.as_view(), name='custom_password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(), name='_password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]