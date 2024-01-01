from django.shortcuts import render

# Create your views here.
def homePageFacturas(request):
    return render(request, 'homePageFacturas.html')