from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def Igresar(request):
    return render(request, 'main/login.html')

def Login(request, username):
    user = authenticate(username=username, password="samk1234")
    if user:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("No es posible ingresar con este usuario. Póngase en contacto con el administrador.")

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/ingresar/')
def Home(request):
    return render(request, 'main/home.html')