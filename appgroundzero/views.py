from django.shortcuts import render
from django.templatetags.static import static
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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


def productos(request):
    context={}
    return render(request, 'gestion/productos_list.html', context)