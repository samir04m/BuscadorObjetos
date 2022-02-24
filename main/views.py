from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

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

from django.db.models import Q

from functools import reduce
import operator

@login_required(login_url='/ingresar/')
def Home(request):
    context = {}
    if request.method == 'POST':
        query = request.POST.get('query')
        words = query.split(' ')
        wordsToSearch = reduce(operator.or_, (Q(name__icontains=w) for w in words))
        
        if request.user.is_superuser:
            # results = Object.objects.filter(Q(name__icontains=query))
            results = Object.objects.filter(wordsToSearch)
        else:
            results = Object.objects.filter( Q(public=1) & Q(wordsToSearch) )
        context['query'] = query
        context['results'] = results

    return render(request, 'main/home.html', context)