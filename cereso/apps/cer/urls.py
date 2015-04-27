from django.conf.urls.defaults import patterns,url 

urlpatterns=patterns('cereso.apps.cer.views',
    url(r'^add/empleado/$','add_empleado_view',name='vista_agregar_empleado'),
    url(r'^edit/empleado/(?P<id_emp>.*)/$','edit_empleado_view',name= "vista_editar_empleado"),
    url(r'^add/institucion/$','add_institucion_view',name='vista_agregar_institucion'),
    url(r'^edit/institucion/(?P<id_in>.*)/$','edit_institucion_view',name= "vista_editar_institucion"),
   

	)