from django.contrib.auth.models import User
from django.db import models
from random import randint

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

	def gera_codigo(self):
		token = ''
		for num in range(0,8):
			char = randint(1,4)
			if char == 1:
				token += str(chr(randint(48,57)))
			elif char == 2:
				token += str(chr(randint(65,90)))
			else:
				token += str(chr(randint(97,122)))
		return token