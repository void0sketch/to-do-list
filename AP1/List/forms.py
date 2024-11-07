from django import forms
from .models import toDolists

class toDolistsForm(forms.ModelForm):
    class Meta :
        model = toDolists
        fields = ['title', 'description', 'completed']
