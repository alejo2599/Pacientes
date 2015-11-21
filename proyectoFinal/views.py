from proyectoFinal.models import Paciente, Comentario
from proyectoFinal.forms import PacienteForm, ComentarioForm, ContactoForm
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#from django.views.generic import TemplateView


# Create your views here.

#class IndexView(TemplateView):
#	template_name = 'base.html'

def inicio(request):
	pacientes = Paciente.objects.all()
	return render_to_response("inicio.html",dict(pacientes = pacientes), context_instance=RequestContext(request))

def usuarios(request):
	usuarios = User.objects.all()
	pacientes = Paciente.objects.all()
	return render_to_response("usuarios.html",{'usuarios':usuarios, 'pacientes':pacientes}, context_instance=RequestContext(request))

def lista_pacientes(request):
	pacientes = Paciente.objects.all()
	return render_to_response("lista_pacientes.html", {'datos':pacientes}, context_instance=RequestContext(request))

def detalle_paciente(request, id_paciente):
	dato = get_object_or_404 (Paciente, pk=id_paciente)
	comentarios = Comentario.objects.filter(paciente=dato)
	return render_to_response("paciente.html", {'paciente':dato, 'comentarios':comentarios}, context_instance=RequestContext(request))

def sobre(request):
	html = "<html><body>Proyecto Final</body></html>"
	return HttpResponse(html)

def contacto(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje desde el Proyecto de Frameworks Web'
			contenido = formulario.cleaned_data ['mensaje'] + "\n"
			contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
			correo = EmailMessage (titulo, contenido, to=['aleju93066@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else: 
		formulario=ContactoForm()
	return render_to_response('contactoform.html', {'formulario':formulario}, context_instance=RequestContext(request))


def nuevo_paciente(request):
	formulario = PacienteForm(request.POST, request.FILES)
	if request.method=='POST':		
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/pacientes')
	else:
		formulario = PacienteForm()
	return render_to_response('pacienteform.html', {'formulario':formulario}, context_instance=RequestContext(request))


def nuevo_comentario(request):
	if request.method=='POST':
		formulario = ComentarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/pacientes')
	else:
		formulario=ComentarioForm()
	return render_to_response('comentarioform.html', {'formulario':formulario}, context_instance=RequestContext(request))


#Crear usuarios sin la interfaz de Django utilizando UserCreationForm
def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=UserCreationForm()
	return render_to_response('nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request))


#Interfaz de ingreso al sistema utilizando AuthenticationForm
def ingresar(request):
	#El formulario de registro de usuario no aparece mientras un usuario ya este dentro del sistema
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid():
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				#is_activate demuestra si el usuario exista en sistema, pero debe estar activo para ingresar
				if acceso.is_active():
					login(request, acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

#Restriccion de autenticacion, se debe ingresar al sistema para poder observar el contenido utilizando login_required
@login_required(login_url='/ingresar') #Activa la restriccion
def privado(request):
    usuario = request.user
    return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

#al tener un login_required obliga a tener un cierre de sesion, para el cual se utiliza logout
@login_required(login_url='/ingresar')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')