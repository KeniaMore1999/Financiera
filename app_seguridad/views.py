from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'app_seguridad/index.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                return HttpResponse('existe activo')
            else: 
                return HttpResponse('existe pero no activo')
        else:
            return HttpResponse('No existe')

        return HttpResponse(f'Usuario: {username} - Clave: {password}')
    else:
        return redirect('/')