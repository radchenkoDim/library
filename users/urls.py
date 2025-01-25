from . import views
from django.urls import path, include


#app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile_own, name='profile'),
    path('profile/<int:user_id>/', views.profile_user, name='profile_user'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit_profile, name='edit_profile'),
]