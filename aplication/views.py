from django.shortcuts import render
from .models import *
from django.views.generics import CreateView
# Create your views here.

class DisciplinaView(CreateView):
    
    form_class=DisciplinaForm
    success_url="/"
    template_name="adicionar_disciplina.html"
    model=Disciplina
