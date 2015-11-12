from django.shortcuts import render

# Create your views here.

def FC_Social_template(request):
    return render(request, 'home.html')

def reg(request):
    return render(request, 'registro.html')

