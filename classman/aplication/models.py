from django.contrib.auth.models import User
from django.db import models

class Professor(models.Model):
	usuario = models.OneToOneField(User, related_name='professor', on_delete=models.CASCADE)
	matricula = models.CharField(max_length=8, unique=True)
	def __str__(self):
		return self.usuario.username

class Disciplina(models.Model):
	professor = models.ManyToManyField(Professor)
	codigo_acesso = models.CharField(max_length=8, unique=True)
	nome = models.CharField(max_length=60)
	descricao = models.TextField(null=True)
	ementa = models.TextField(null=True)
	data_inicio = models.DateTimeField(auto_now_add=False)
	data_fim = models.DateTimeField(auto_now_add=False)
	def __str__(self):
		return self.nome
