from django.contrib.auth.models import User
from django.test import TestCase
from .models import *

class TestDisciplina(TestCase):
	def test_criar_disciplina(self):
		dis = Disciplina(codigo_acesso="ukjyhbs", nome="Engenharia",descricao="Engenharia de Software II", data_inicio='2019-04-15', data_fim='2019-05-25')
		self.assertIs(dis.__str__(), "Engenharia")

class TestProfessor(TestCase):
	def test_cria_professor(self):
		user = User(username="Carlos", email="carlos@email", password="123456")
		user.save()
		prof = Professor(usuario=user, matricula="458745TR")
		self.assertIs(prof.__str__(),"Carlos")