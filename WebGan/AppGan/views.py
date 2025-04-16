from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

def inicio(request):
    return render(request, 'inicio.html')

def noticias(request):
    return render(request, 'noticias.html')

def foro(request):
    return render(request, 'foro.html')

def compra_venta(request):
    return render(request, 'compra_venta.html')

def mi_ganado(request):
    return render(request, 'mi_ganado.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("inicio")  # Redirige al inicio después del login
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "login.html")

def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Tu cuenta ha sido creada exitosamente!")
            return redirect("login")  # Redirige al login después del registro
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})

def acerca_de_nosotros(request):
    return render(request, 'acerca_de_nosotros.html')

@login_required
def perfil_view(request):
    return render(request, "perfil.html", {"user": request.user})