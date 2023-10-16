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
class   EditProfileForm(UserChangeForm):
    email=forms.EmailInput(attrs={'class': 'form-control'})
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    data_joined=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','last_login','data_joined')
    
class ProfileUser(forms.ModelForm):
    class Meta():
        model = Profail
        fields = ('user','firstname','lastname', 'photo', 'address','phone_number')
        # widgets = {
        #     'user': forms.TextInput(attrs={'class': 'user'}),
        #     'firstname': forms.TextInput(attrs={'class': 'firstname'}),
        #     'lastname': forms.TextInput(attrs={'class': 'lastname'}),
        #     'photo': forms.TextInput(attrs={'class': 'photo'}),
        #     'address': forms.TextInput(attrs={'class': 'address'}),
        #     'phone_number': forms.TextInput(attrs={'class': 'phone_number'}),
        # }