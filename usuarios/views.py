from django.shortcuts import render

def index(request):
    return render(request, 'usuarios/usuarios.html')

def login_usuario(request):
    return render(request, 'usuarios/usuarios.html')

def cadastro_usuario(request):
    return render(request, 'usuarios/cadastre-se.html')