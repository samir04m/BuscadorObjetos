from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Q
from functools import reduce
import operator
from .models import *

class CustomLoginView(LoginView):
    template_name = 'main/login.html'

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def Home(request):
    query = request.GET.get('query', '')
    context = {'query': query}

    if query:
        words = query.split()
        wordsToSearch = reduce(operator.or_, (Q(name__icontains=w) for w in words))

        if request.user.is_superuser:
            results = Object.objects.filter(wordsToSearch)
        else:
            results = Object.objects.filter(Q(public=True) & wordsToSearch)

        paginator = Paginator(results, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['results'] = page_obj

    return render(request, 'main/home.html', context)

# def Home(request):
#     context = {}
#     if request.method == 'POST':
#         query = request.POST.get('query')
#         words = query.split(' ')
#         wordsToSearch = reduce(operator.or_, (Q(name__icontains=w) for w in words))
        
#         if request.user.is_superuser:
#             # results = Object.objects.filter(Q(name__icontains=query))
#             results = Object.objects.filter(wordsToSearch)
#         else:
#             results = Object.objects.filter( Q(public=1) & Q(wordsToSearch) )

#         paginator = Paginator(results, 1)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)

#         context['query'] = query
#         context['results'] = page_obj

#     return render(request, 'main/home.html', context)

@login_required
def Details(request, id):
    if request.user.is_superuser:
        object = get_object_or_404(Object, id=id)
    else:
        object = get_object_or_404(Object, id=id, public=1)


    log = ViewLog.objects.filter(user=request.user, object=object).first()
    if log:
        log.last_seen = datetime.now()
    else:
        log = ViewLog(
            user = request.user,
            object = object,
            last_seen = datetime.now()
        )
    log.save()

    return render(request, 'main/details.html', { 'object':object })

@login_required
def MySearches(request):
    all_searches = ViewLog.objects.filter(user=request.user).order_by('-last_seen')
    paginator = Paginator(all_searches, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/mysearches.html', { 'page_obj': page_obj })
