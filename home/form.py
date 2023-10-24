from django import forms
from .models import Contact,Post,Comment



    

class ContactForm(forms.ModelForm):
    class Meta():
        model=Contact
        fields="__all__"

class UpdateForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('name', 'title', 'body','category')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
            'title': forms.TextInput(attrs={'class': 'title'}),
            'body': forms.TextInput(attrs={'class': 'body'}),
            'catecory': forms.TextInput(attrs={'class': 'catecory'}),
            
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')