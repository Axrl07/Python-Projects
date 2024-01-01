from django.shortcuts import render

# Create your views here.
def homePageReportes(request):
    return render(request, 'homePageReportes.html')