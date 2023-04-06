from django import forms
from .models import ApplyReq
from django.forms import ModelForm , TextInput, ClearableFileInput

class ApplyForm(forms.ModelForm):
    class Meta:
        # sexChoices =(
        #     (1, "Male")
        #     (2, "Female")
        # )


        model = ApplyReq
        fields = ['firstName','lastName', 'email', 'age', 'phone','location','cv','linkedIn', 'cover']
        widgets = {
            'firstName' : TextInput(attrs={
                'class' : 'input',
            }),
            'lastName' : TextInput(attrs={
                'class' : 'input',
            }),
            'email' : TextInput(attrs={
                'class' : 'input',
            }),
            'age' : TextInput(attrs={
                'class' : 'input',
            }),
            'phone' : TextInput(attrs={
                'class' : 'input',
            }),
            'location' : TextInput(attrs={
                'class' : 'input',
            }),
            'cv' : ClearableFileInput(attrs={
                'class' : 'input',
            }),
            'linkedIn' : TextInput(attrs={
                'class' : 'input',
            }),
            'cover' : TextInput(attrs={
                'class' : 'input',
            }),
        }       