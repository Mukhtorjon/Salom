from typing import Any
from django.db import models
from django.shortcuts import render,redirect
from django.views import generic
from .forms import SingnUpForm,EditProfileForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profail
from django.contrib.messages import success

# from django.contrib.auth import User
class UserRegisterView(generic.CreateView):
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    form_class=SingnUpForm
def profil(request):
    context={}
    context['profil']=Profail.objects.get(user=request.user)
    return render(request, "registration/profile.html",context)
  

def update_view(request,pk):
    if request.method == 'POST':
        p_form = EditProfileForm(request.POST, request.FILES,instance=request.user.profail)
        if p_form.is_valid():
            p_form.save()
            success(request, f'Account Successfully Updated!')
            return redirect('profile')

    else:
        p_form = EditProfileForm(instance=request.user.profail)

    context = {
        'form' : p_form
    }
    return render(request, 'registration/edit_profile.html', context)
class UpdateProfile(generic.UpdateView):
    model=Profail
    template_name='registration/edit_profile.html'
    context_object_name='form'
    form_class=EditProfileForm
    success_url=reverse_lazy('profile')
class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    template_name='registration/change_password.html'
    success_url=reverse_lazy('index')





# RYKXBGYWLVABJMX5WUZEXW2X