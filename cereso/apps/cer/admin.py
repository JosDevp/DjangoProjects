from django.contrib import admin
from cereso.apps.cer.models import empleado,institucion,situacion,delito,fuero,clasificacion,posicion,departamentoEmpleado,Category,proyecto



class empleadoAdmin(admin.ModelAdmin):
	list_display = ('nombre','thumbnail','apellidop','apellidom')
	list_filter = ('nombre','apellidop')
	search_fields = ['nombre','apellidop']
	fields = ('nombre','apellidop',('apellidom','direccion','imagen'),'departamentos')




admin.site.register(empleado,empleadoAdmin)
admin.site.register(institucion)
admin.site.register(situacion)
admin.site.register(delito)
admin.site.register(fuero)
admin.site.register(clasificacion)
admin.site.register(posicion)
admin.site.register(departamentoEmpleado)
admin.site.register(Category)
admin.site.register(proyecto)

