from django.shortcuts import render

# Create your views here.

def homePageProductos(request):
    return render(request, 'homePageProductos.html')

def obtenerProductos(request):
    pass
    