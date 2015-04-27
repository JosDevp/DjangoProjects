from django .shortcuts import render_to_response
from django.template import RequestContext
from cereso.apps.cer.forms import addEmpleadoForm,addInstitucionForm
from cereso.apps.cer.models import empleado,institucion
from django.http import HttpResponseRedirect




def add_empleado_view(request):
	info = "iniciado"
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addEmpleadoForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.status = True
				add.save() # Guardamos la informacion
				form.save_m2m() # Guarda las relaciones de ManyToMany
				info = "Guardado satisfactoriamente"
				return HttpResponseRedirect('/empleado/%s'%add.id)
		else:
			form = addEmpleadoForm()
		ctx = {'form':form,'informacion':info}
		return render_to_response('cer/addEmpleados.html',ctx,context_instance=RequestContext(request)) 
	else:
		return HttpResponseRedirect('/')

		


def edit_empleado_view(request,id_emp):
	info = "iniciado"
	e = empleado.objects.get(pk=id_emp)
	if request.method == "POST":
		form = addEmpleadoForm(request.POST,request.FILES,instance=e)
		if form.is_valid():
			edit_emp = form.save(commit=False)
			form.save_m2m()
			edit_emp.status = True
			edit_emp.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/empleado/%s/'%edit_emp.id)
	else:
		form = addEmpleadoForm(instance=e)
	ctx = {'form':form,'informacion':info}
	return render_to_response('cer/editEmpleado.html',ctx,context_instance=RequestContext(request))


"""
def add_empleado_view(request):
	info = "Inicializando" 
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addEmpleadoForm(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				apellidop =form.cleaned_data['apellidop']
				apellidom =form.cleaned_data['apellidom']
				direccion=form.cleaned_data['direccion']
				zip=form.cleaned_data['zip']
				sexo=form.cleaned_data['sexo']
				imagen=form.cleaned_data['imagen']
				fecha=form.cleaned_data['fecha']
				notas=form.cleaned_data['notas']
				contratacion=form.cleaned_data['contratacion']
				faltas=form.cleaned_data['faltas']
				salario=form.cleaned_data['salario']
				empleo =form.cleaned_data['empleo']

				
				j           =empleado()	
				
			    	
				
				
				j.nombre 		=  nombre
				j.apellidop = apellidop
				j.apellidom= apellidom
				
				j.direccion=direccion
				j.zip=zip
				j.sexo=sexo
				j.imagen = imagen
				j.fecha=fecha
				j.notas=notas
				j.contratacion=contratacion
				j.faltas=faltas
				j.salario=salario
				j.empleo=empleo 
				j.save() # Guardar la informacion
				info = "Se guardo satisfactoriamente!!!!!"
			else:
				info = "informacion con datos incorrectos"			
		form = addEmpleadoForm()
		ctx = {'form':form, 'informacion':info}
		return render_to_response('cer/addEmpleados.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


"""
"""
def edit_empleado_view(request,id_emp):
	info = ""
	e = empleado.objects.get(id=id_emp)
	if request.method == "POST":
		form = addEmpleadoForm(request.POST,request.FILES)
		if form.is_valid():
				nombre = form.cleaned_data['nombre']
				apellidop =form.cleaned_data['apellidop']
				apellidom =form.cleaned_data['apellidom']
				direccion=form.cleaned_data['direccion']
				zip=form.cleaned_data['zip']
				sexo=form.cleaned_data['sexo']
				imagen=form.cleaned_data['imagen']
				fecha=form.cleaned_data['fecha']
				notas=form.cleaned_data['notas']
				contratacion=form.cleaned_data['contratacion']
				faltas=form.cleaned_data['faltas']
				salario=form.cleaned_data['salario']
				empleo =form.cleaned_data['empleo']
				e.nombre 		=  nombre
				e.apellidop 	= apellidop
				e.apellidom 		= apellidom
				e.direccion 		= direccion
				e.zip=zip
				e.sexo=sexo
				e.imagen = imagen
				e.fecha=fecha
				e.notas=notas
				e.contratacion=contratacion
				e.faltas=faltas
				e.salario=salario
				e.empleo=empleo
				
				e.save() # Guardar la informacion
				info = "Se guardo satisfactoriamente!!!!!"
				return HttpResponseRedirect('/empleado/%s'%e.id)
	if request.method == "GET":
		form = addEmpleadoForm(initial={
									'nombre':e.nombre,
									'apellidop':e.apellidop,
									'apellidom':e.apellidom,
									'direccion':e.direccion,
									'zip':e.zip,
									'sexo':e.sexo,
									'fecha':e.fecha,
									'notas':e.notas,
									'contratacion':e.contratacion,
									'faltas':e.faltas,
									'salario':e.salario,
								    'empleo':e.empleo
								    
			})
	ctx = {'form':form,'info':info,'empleado':e}
	return render_to_response('cer/editEmpleado.html',ctx,context_instance=RequestContext(request))
"""	



def add_institucion_view(request):
	info = "Inicializando" 
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addInstitucionForm(request.POST,request.FILES)
			if form.is_valid():
				descripcion = form.cleaned_data['descripcion']
				

				
				j           =institucion()	
				
			    	
				
				
				j.descripcion 		=  descripcion
			
				j.save() # Guardar la informacion
				info = "Se guardo satisfactoriamente!!!!!"
			else:
				info = "informacion con datos incorrectos"			
		form = addInstitucionForm()
		ctx = {'form':form, 'informacion':info}
		return render_to_response('cer/addInstitucion.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')



def edit_institucion_view(request,id_in):
	info = ""
	e = institucion.objects.get(id=id_in)
	if request.method == "POST":
		form = addInstitucionForm(request.POST,request.FILES)
		if form.is_valid():
				descripcion = form.cleaned_data['descripcion']
				
				e.descripcion		=  descripcion
			
				
				e.save() # Guardar la informacion
				info = "Se guardo satisfactoriamente!!!!!"
				return HttpResponseRedirect('/institucion/%s'%e.id)
	if request.method == "GET":
		form = addInstitucionForm(initial={
									'descripcion':e.descripcion
									
								    
			})
	ctx = {'form':form,'info':info,'institucion':e}
	return render_to_response('cer/editInstitucion.html',ctx,context_instance=RequestContext(request))




	
