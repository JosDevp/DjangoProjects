from django import forms
from django.forms.extras.widgets import SelectDateWidget
from cereso.apps.cer.models import empleado 






class addEmpleadoForm(forms.ModelForm):
	class Meta:
		model   = empleado
		exclude = {'status',}


                          
                       
"""
class addEmpleadoForm(forms.Form):
	nombre=forms.CharField(label="Nombre:",widget=forms.TextInput())
	apellidop=forms.CharField(label="Apellido Paterno:",widget=forms.TextInput())
	apellidom=forms.CharField(label="Apellido Materno:",widget=forms.TextInput())
	direccion=forms.CharField(label="Direccion:",widget=forms.Textarea())
	zip=forms.CharField(label="Codigo Postal:",widget=forms.TextInput())
	sexo=forms.CharField(label="Sexo:",widget=forms.TextInput())
	imagen 		= forms.ImageField(required=False)
	#fecha =forms.CharField(widget=forms.TextInput())
	fecha = forms.CharField(label="Fecha de Nacimiento:",widget=SelectDateWidget())
	notas =forms.CharField(label="Notas:",widget=forms.Textarea())
	#contratacion=forms.CharField(widget=forms.TextInput())
	contratacion = forms.DateField(label="Fecha Contratacion",widget=SelectDateWidget())
	faltas		= forms.IntegerField(label="Faltas:",widget=forms.TextInput())
	salario		= forms.IntegerField(label="Salario:",widget=forms.TextInput())
	empleo=forms.CharField(label="Tipo Empleo:",widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data
"""

CHOICES = (
    (0, 'Masculino'), 
    (1, 'Femenino'), 
    
)

class addInstitucionForm(forms.Form):
	descripcion=forms.CharField(label="Nombre Institucion:",widget=forms.Textarea())	
	choice_field = forms.ChoiceField(choices=CHOICES)
	#radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    #multiple_choice = forms.MultipleChoiceField(choices=CHOICES)

	def clean(self):
		return self.cleaned_data






