from django.shortcuts import render
from .models import Pelicula, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.

def home(request):
    #peliculas = Pelicula.objects.filter(estado=True)
    peliculas = Pelicula.objects.all()
    last = Pelicula.objects.all().order_by('-id')[:1]
    last_ten = Pelicula.objects.all().order_by('-id')[:12]
    
    pelicula_accion = Pelicula.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre='Accion')
    )
    pelicula_animadas = Pelicula.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre='Animacion')
    )
    pelicula_superheroe = Pelicula.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre='Superheroes')
    )
    pelicula_terror = Pelicula.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre='Terror')
    )

    data = {
        'peliculas': peliculas,
        'last': last,
        'last_ten': last_ten,
        'accion': pelicula_accion,
        'animadas': pelicula_animadas,
        'superheroes': pelicula_superheroe,
        'terror': pelicula_terror,
    }
    return render(request, 'index.html', data)


def verPost(request, slug):
    pelicula = Pelicula.objects.get(
        slug=slug
    )

    data = {
        'detalle_post': pelicula,
    }


    return render(request, 'detalle_pelicula.html', data)

def peliculas(request):
    queryset = request.GET.get("buscar")
    todas = Pelicula.objects.filter(estado=True).order_by('-id')
    data = {
        'peliculas': todas,
    }
    
    if queryset:
        buscar = Pelicula.objects.filter(
            Q(titulo__icontains = queryset)
        ).distinct()
        data = {
            'peliculas': buscar,
            'busqueda': queryset,
        }


    return render(request, 'peliculas.html', data)


def series(request):
    todas = Pelicula.objects.all().order_by('-id')
    data = {
        'series': todas,
    }
    return render(request, 'series.html', data)