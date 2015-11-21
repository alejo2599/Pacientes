#encoding:utf-8
from django.forms import ModelForm
from django import forms
from proyectoFinal.models import Paciente, Comentario

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electronico')
	mensaje = forms.CharField(widget=forms.Textarea)

class PacienteForm(ModelForm):
	class Meta: 
		model = Paciente
		fields = '__all__'

class ComentarioForm(ModelForm):
	class Meta:
		model = Comentario
		fields = '__all__'