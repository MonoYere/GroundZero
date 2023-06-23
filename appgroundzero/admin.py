from django.contrib import admin
from .models import Producto, Artista, Categoria

# Register your models here.
admin.site.register(Artista)
admin.site.register(Categoria)
admin.site.register(Producto)