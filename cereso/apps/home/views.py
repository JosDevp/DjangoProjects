from  django.shortcuts import render_to_response
from django.template import RequestContext
from cereso.apps.cer.models import empleado,institucion,proyecto
from cereso.apps.home.forms import ContactoForm, LoginForm,RegisterForm
from django.core.mail import EmailMultiAlternatives # Enviamos HTML
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
import django
from cereso.settings import URL_LOGIN
# Paginacion en Django
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.decorators import login_required
import json



def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def about_view(request):
    
	mensaje="@rgusbemus"
	ctx={'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))


def empleado_view(request,pagina):
	if request.method=="POST":
		if "product_id" in request.POST:
			try:
				id_emp = request.POST['product_id']
				e = empleado.objects.get(pk=id_emp)
				mensaje = {"status":"True","product_id":e.id}
				e.delete() # Elinamos objeto de la base de datos
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')

	
	lista_emp= empleado.objects.filter()
	paginator = Paginator(lista_emp,3) # Cuantos productos quieres por pagina 1
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		empleados = paginator.page(page)
	except (EmptyPage,InvalidPage):
		empleados = paginator.page(paginator.num_pages)
	ctx={'empleados':empleados}
	return 	render_to_response('home/empleados.html',ctx,context_instance=RequestContext(request))



def singleEmpleado_view(request,id_emp):
	emp = empleado.objects.get(id=id_emp)
	dep=emp.departamentos.all() # Obteniendo las categorias del producto encontrado relacion many to many
	ctx = {'empleado':emp,'departamentos':dep}
	return render_to_response('home/SingleEmpleados.html',ctx,context_instance=RequestContext(request))



def institucion_view(request,pagina):
	
	


		lista_in= institucion.objects.filter()
		paginator = Paginator(lista_in,3) # Cuantos productos quieres por pagina 1
		try:
			page = int(pagina)
		except:
			page = 2
		try:
			instituciones = paginator.page(page)
		except (EmptyPage,InvalidPage):
			instituciones = paginator.page(paginator.num_pages)
		ctx={'instituciones':instituciones}
		return 	render_to_response('home/institucion.html',ctx,context_instance=RequestContext(request))
		


def singleInstitucion_view(request,id_in):
	ints = institucion.objects.get(id=id_in)
	#prod.categorias.all() # Obteniendo las categorias del producto encontrado
	ctx = {'institucion':ints}
	return render_to_response('home/SingleInstitucion.html',ctx,context_instance=RequestContext(request))


	


@login_required(login_url=URL_LOGIN)
def proyecto_view(request,pagina):
	
		lista_po= proyecto.objects.filter()
		paginator = Paginator(lista_po,3) # Cuantos productos quieres por pagina 1
		try:
			page = int(pagina)
		except:
			page = 3
		try:
			proyectos = paginator.page(page)
		except (EmptyPage,InvalidPage):
			proyectos = paginator.page(paginator.num_pages)
		ctx={'proyectos':proyectos}
		return 	render_to_response('home/proyectos.html',ctx,context_instance=RequestContext(request))


def singleProyecto_view(request,id_po):
	pro = proyecto.objects.get(id=id_po)
	#prod.categorias.all() # Obteniendo las categorias del producto encontrado
	ctx = {'proyecto':pro}
	return render_to_response('home/SingleProyectos.html',ctx,context_instance=RequestContext(request))








@login_required(login_url=URL_LOGIN)
def contacto_view(request):
	info_enviado = False # Definir si se envio la informacion o no se envio
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			# Configuracion enviando mensaje via GMAIL
			to_admin = 'josegpe7hdez@gmail.com'
			html_content = "Informacion recibida de [%s] <br><br><br>***Mensaje****<br><br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
			msg.send() # Enviamos  en correo
	else:
		formulario = ContactoForm()
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))




def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				next = request.POST['next']
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect(next)
				else:
					mensaje = "usuario y/o password incorrecto"
		next = request.REQUEST.get('next')
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje,'next':next}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')





def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save() # Guardar el objeto
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return 	render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))	


def servicio_view(request):
	return render_to_response('home/servicios.html',context_instance=RequestContext(request))
