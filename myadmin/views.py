from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from datetime import datetime
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
def AdminSubcontainer(request, id):
    subcontainer = object = get_object_or_404(Subcontainer, id=id)
    return render(request, 'admin/adminSubcontainer.html', { 'subcontainer':subcontainer })

@login_required(login_url='/ingresar/')
def CreateObject(request):
    if request.method == 'POST':
        public = 1 if request.POST.get('public') else 0
 
        obj = Object(
            name = request.POST.get('name'),
            subcontainer_id = int(request.POST.get('subcontainer_id')),
            photo = request.FILES.get('photo'),
            public = public,
            details =  request.POST.get('details'),
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        obj.save()

    return redirect('myadmin:adminsubcontainer', int(request.POST.get('subcontainer_id')))