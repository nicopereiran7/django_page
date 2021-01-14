from django.urls import path
from .views import home, verPost, peliculas, series

urlpatterns =[
    path('', home, name='Home'),
    path('<slug:slug>/', verPost, name='detalle_post'),
    path('peliculas', peliculas, name='peliculas'),
    path('series', series, name='series'),
] 