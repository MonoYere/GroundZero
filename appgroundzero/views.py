from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Producto
from .models import Artista
from .models import Categoria
from .forms import ProductoForm

# Create your views here.
def index(request):
    context={}
    return render(request, 'groundzero/index.html', context)

def acerca_de(request):
    context={}
    return render(request, 'groundzero/acerca-de.html', context)

def artistas(request):
    context={}
    return render(request, 'groundzero/artistas.html', context)

def contacto(request):
    return render(request, 'groundzero/contacto.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion/productos_list.html', {'productos': productos})

def agregar(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'gestion/productos_add.html', {'formulario': formulario})

def editar(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('productos')
    return render(request, 'gestion/productos_edit.html', {'formulario':formulario})
    

def eliminar(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect('productos')