from django import forms

def should_be_empty():
    raise forms.ValidationError('Field is not empty')

class FormContact(forms.Form):
    name=forms.CharField(max_length=200)
    message=forms.CharField(widget=forms.Textarea)
    email=forms.EmailInput()
    forcefield=forms.CharField(required=False,widget=forms.HiddenInput,label="Leave empty",validators=[should_be_empty])
    