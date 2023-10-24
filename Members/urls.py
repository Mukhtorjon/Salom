from django.urls import path
from .views import UserRegisterView,profil,PasswordChangeView,UpdateProfile,update_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/<int:pk>/',update_view,name='edit_profile'),
    path('profile/',profil,name='profile'),
    path('password/',PasswordChangeView.as_view(),name='change_password'),
    
   
    
]   
 