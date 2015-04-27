from django.db import models


class proyecto(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Proyecto/%s/%s"%(self.nombre,str(filename))
		return ruta


	nombre=models.CharField(max_length=100)
	imagen 		= models.ImageField(upload_to=url,null=True,blank=True)
	descripcion=models.TextField(max_length=500)
	link=models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre




class departamentoEmpleado(models.Model):

	nombre =models.CharField(max_length=200)
	descripcion=models.TextField(max_length=300)


	def __unicode__(self):
		return self.nombre



class empleado(models.Model):
	SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        
    )


	
	def url(self,filename):
		ruta = "MultimediaData/Empleado/%s/%s"%(self.nombre,str(filename))
		return ruta

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)


		thumbnail.allow_tags = True

	nombre = models.CharField("Nombre:",max_length=200)
	apellidop = models.CharField("Apellido Paterno:",max_length=200)
	apellidom=models.CharField("Apellido Materno:",max_length=200)
	direccion=models.TextField("Direccion:",max_length=300)
	zip=models.CharField("Codigo Postal:",max_length=20)
	sexo=models.CharField("Sexo:",max_length=50,choices=SEXO)
	imagen 		= models.ImageField(upload_to=url,null=True,blank=True)
	fecha =models.CharField("Fecha Nacimiento:",max_length=30)
	notas =models.CharField("Notas:",max_length=300)
	contratacion=models.CharField("Fecha Contratacion:",max_length=30)
	faltas		= models.IntegerField()
	salario		= models.IntegerField()
	empleo=models.CharField("Tipo Empleo:",max_length=50)
	departamentos=models.ManyToManyField(departamentoEmpleado,null=True,blank=True)
	

	def __unicode__(self):
		nombreC="%s %s"%(self.nombre,self.apellidop)
		return nombreC






class institucion(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.TextField(max_length=400)

	def __unicode__(self):
		return self.nombre


class situacion(models.Model):
	nombre=models.CharField(max_length=100)

	descripcion=models.TextField(max_length=400)


	def __unicode__(self):
		return self.nombre


class delito (models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.TextField(max_length=400)

	def __unicode__(self):
		return self.nombre



class fuero (models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.TextField(max_length=400)

	def __unicode__(self):
		return self.nombre


class clasificacion (models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.TextField(max_length=400)

	def __unicode__(self):
		return self.nombre

class posicion (models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.TextField(max_length=400)

	def __unicode__(self):
		return self.nombre


class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True,
	help_text='Unique value for product page URL, created from name.')
	description = models.TextField()
	is_active = models.BooleanField(default=True)
	meta_keywords = models.CharField("Meta Keywords",max_length=255,
	help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField("Meta Description", max_length=255,
	help_text='Content for description meta tag')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name
		



		








		




