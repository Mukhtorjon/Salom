from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from .models import Profail


class   SingnUpForm(UserCreationForm):
    email=forms.EmailField()
    # first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    def __init__(self, *args, **kwargs):
        super(SingnUpForm,self).__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
# class   EditProfileForm(forms.ModelForm):
#     email=forms.EmailInput(attrs={'class': 'form-control'})
#     first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_login=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     # is_superuser=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
#     # is_staff=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
#     # is_active=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
#     # data_joined=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  
    # class Meta:
    #     model=Profail
    #     fields = '__all__'
    #     exclude=['user']
    
class EditProfileForm(forms.ModelForm):
    # photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta():
        model = Profail
        fields = "__all__"
       
# class UserUpdateForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name']

# class ProfileUpdateForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=32)
#     last_name = forms.CharField(max_length=32)
#     class Meta:
#         model = Profail
#         fields = ['photo']