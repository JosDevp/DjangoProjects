from django.conf.urls.defaults import patterns, url

urlpatterns=patterns('cereso.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	#url(r'^empleado/$','empleado_view',name='vista_empleado'),
	url(r'^empleado/page/(?P<pagina>.*)/$','empleado_view',name='vista_empleado'),
	url(r'^empleado/(?P<id_emp>.*)/$','singleEmpleado_view',name='vista_single_empleado'),
	url(r'^institucion/page/(?P<pagina>.*)/$','institucion_view',name='vista_institucion'),
	url(r'^institucion/(?P<id_in>.*)/$','singleInstitucion_view',name='vista_single_institucion'),
    url(r'^contacto/$','contacto_view',name='vista_contacto'),
    url(r'^login/$','login_view',name='vista_login'),
    url(r'^logout/$','logout_view',name='vista_logout'),
    url(r'^registro/$','register_view',name='vista_registro'),
    url(r'^servicios/$','servicio_view',name='vista_servicio'),
    url(r'^proyecto/page/(?P<pagina>.*)/$','proyecto_view',name='vista_proyecto'),
    url(r'^proyecto/(?P<id_po>.*)/$','singleProyecto_view',name='vista_single_proyecto'),


	)

