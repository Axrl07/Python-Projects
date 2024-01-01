from django.shortcuts import render

# Create your views here.
def homePageClientes(request):
    return render(request, 'homePageClientes.html')