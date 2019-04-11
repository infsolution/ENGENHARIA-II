from .models import *
from django import forms

class DisciplinaForm(forms.ModelForm):

    class Meta:
        model=Disciplina
        fields='__all__'