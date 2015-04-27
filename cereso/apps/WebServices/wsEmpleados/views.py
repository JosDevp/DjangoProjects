# Create your views here.
from django.http import HttpResponse
from cereso.apps.cer.models import empleado, institucion
# Integramos la serializacion de los objetos
from django.core import serializers



def wsEmpleados_view(request):
	data = serializers.serialize("json",empleado.objects.filter())
	# Retorna la informacion en formato json
	return HttpResponse(data,mimetype='application/json')



def wsInstituciones_view(request):
	data = serializers.serialize("json",institucion.objects.filter())
	# Retorna la informacion en formato json
	return HttpResponse(data,mimetype='application/json')
			