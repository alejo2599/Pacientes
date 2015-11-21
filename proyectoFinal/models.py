#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):
	cedula = models.CharField(max_length = 10, verbose_name='Cedula', unique=True)
	nombres = models.CharField(max_length=30, verbose_name='Nombres', unique=True)
	apellidos = models.CharField(max_length=30, verbose_name='Apellidos', unique=True)
	celular = models.CharField(max_length = 10, verbose_name='Celular', unique=True)
	usuario = models.ForeignKey(User)

	#Retorna el nombre de cada Paciente para que sea mas legible
	def __str__(self):
		return self.nombres 
		

class Comentario(models.Model):
	paciente = models.ForeignKey(Paciente)
	texto = models.CharField(max_length=200, verbose_name='Comentario')

	def __str__(self):
		return self.texto