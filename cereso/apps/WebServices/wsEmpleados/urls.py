from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('cereso.apps.WebServices.wsEmpleados.views',
	url(r'^ws/empleados/$','wsEmpleados_view',name= "ws_empleados_url"),
	url(r'^ws/institucion/$','wsInstituciones_view',name= "ws_institucion_url"),
)