from django.shortcuts import render

# Create your views here.

def FC_Social_template(request):
    return render(request, 'home.html')

def reg(request):
    return render(request, 'registro.html')

def ini(request):
	return render(request,'inicio.html')

def perfil(request):
	return render(request,'Profile.html')

