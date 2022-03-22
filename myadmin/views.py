from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import *

@login_required(login_url='/ingresar/')
def AdminHome(request):
    rooms = Room.objects.all()
    return render(request, 'admin/adminHome.html', { 'rooms':rooms })

@login_required(login_url='/ingresar/')
def AdminRoom(request, id):
    room = object = get_object_or_404(Room, id=id)
    return render(request, 'admin/adminRoom.html', { 'room':room })

@login_required(login_url='/ingresar/')
def CreateObject(request):
    rooms = Room.objects.all()
    return render(request, 'admin/createObject.html', { 'rooms':rooms })