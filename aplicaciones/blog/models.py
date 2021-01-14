from django.db import models
from ckeditor.fields import RichTextField
from django import forms
from django.core.validators import *

from django.core.files.storage import FileSystemStorage
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoria Activada/Categoria No Activada', default=True)
    fecha_creacion = models.DateField('Fecha Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class OverwriteStorage(FileSystemStorage):
       def _save(self, name, content):
           if self.exists(name):
               self.delete(name)
           return super(OverwriteStorage, self)._save(name, content)

       def get_available_name(self, name):
           return name

class Pelicula(models.Model):
    titulo = models.CharField('Titulo de la Pelicula', max_length=100, null=False, blank=False)
    director = models.CharField('Director de la Pelicula', max_length=100, null=True, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False) 
    descripcion = RichTextField(null=True)
    anio = models.IntegerField('Año de la Pelicula', validators=[MinValueValidator(1900),MaxValueValidator(9999)], null=True, blank=False)
    imagen_fondo = models.ImageField(upload_to='fondos_peliculas', storage=OverwriteStorage())
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True) 
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'

    def __str__(self):
        return self.titulo


class Serie(models.Model):
    titulo = models.CharField('Titulo de la Serie', max_length=100, null=False, blank=False)
    director = models.CharField('Director de la Serie', max_length=100, null=True, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False) 
    descripcion = RichTextField(null=True)
    anio = models.IntegerField('Año de la Emision', validators=[MinValueValidator(1900),MaxValueValidator(9999)], null=True, blank=False)
    imagen_fondo = models.ImageField(upload_to='fondos_series', storage=OverwriteStorage())
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True) 
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.titulo

