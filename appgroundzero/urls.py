#from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('acerca_de', views.acerca_de, name='acerca-de'),
    path('artistas', views.artistas , name="artistas"),
    path('productos', views.productos,name='productos'),
    path('contacto', views.contacto, name='contacto'),
    path('agregar', views.agregar, name='agregar'),
    path('editar', views.editar,name='editar'),
    path('eliminar/<int:id_producto>',views.eliminar, name='eliminar'),
    path('editar/<int:id_producto>', views.editar, name='editar'),
    path('salir/', views.salir, name="salir"),
    path('login', views.login, name="login"),
  

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

