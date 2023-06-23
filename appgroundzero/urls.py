#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('acerca_de', views.acerca_de, name='acerca-de'),
    path('artistas', views.artistas , name="artistas"),
    path('Productos', views.productos,name='productos'),
]

