from django.contrib import admin
from .models import *
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion') 

class PeliculaAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','anio','categoria','estado','fecha_creacion')

class SerieAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','anio','categoria','estado','fecha_creacion')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Serie, SerieAdmin)