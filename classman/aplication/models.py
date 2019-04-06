from django.contrib.auth.models import User
from django.db import models

class Professor(models.Model):
	usuario = models.OneToOneField(User, related_name='professor', on_delete=models.CASCADE)
	matricula = models.CharField(max_length=8, unique=True)
	