from django import forms
from . import models

class SettingsForm(forms.ModelForm):
    Urgent = forms.BooleanField(required=False,label='Urgent')
    Important = forms.BooleanField(required=False,label='Imp')

    class Meta:
        model = models.TodoItem