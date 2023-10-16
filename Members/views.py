from typing import Any
from django.db import models
from django.shortcuts import render
from django.views import generic
from .forms import SingnUpForm,EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# from django.contrib.auth import User
class UserRegisterView(generic.CreateView):
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    form_class=SingnUpForm
    


    

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('index')
    def get_object(self):
        return self.request.user
class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    template_name='registration/change_password.html'
    success_url=reverse_lazy('index')