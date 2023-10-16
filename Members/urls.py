from django.urls import path
from .views import UserRegisterView,UserEditView,PasswordChangeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('password/',PasswordChangeView.as_view(),name='change_password'),
    
   
 
]   
 