from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from main.models import *

@login_required
def AdminHome(request):
    rooms = Room.objects.all()
    return render(request, 'admin/adminHome.html', { 'rooms':rooms })

@login_required
def AdminRoom(request, id):
    room = object = get_object_or_404(Room, id=id)
    return render(request, 'admin/adminRoom.html', { 'room':room })

@login_required
def AdminSubContainer(request, id):
    subContainer = object = get_object_or_404(SubContainer, id=id)
    if request.user.is_superuser:
        objects = subContainer.object_set.all()
    else:
        objects = subContainer.object_set.filter(public=1)
    context = { 'subContainer':subContainer, 'objects':objects }
    return render(request, 'admin/adminSubcontainer.html', context)

@login_required
def CreateObject(request):
    if request.method == 'POST':
        public = True if request.POST.get('public') else False

        obj = Object(
            name = request.POST.get('name'),
            subContainer_id = int(request.POST.get('subContainer_id')),
            photo = request.FILES.get('photo'),
            public = public,
            details =  request.POST.get('details')
        )
        obj.save()

    return redirect('myadmin:adminsubcontainer', int(request.POST.get('subContainer_id')))

@login_required
def CreateRoom(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            obj = Room(
                name = name,
                photo = request.FILES.get('photo')
            )
            obj.save()
    return redirect('myadmin:adminhome')

@login_required
def CreateContainer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            obj = Container(
                name = request.POST.get('name'),
                photo = request.FILES.get('photo'),
                room_id = int(request.POST.get('room_id')),
            )
            obj.save()
    return redirect('myadmin:adminroom', int(request.POST.get('room_id')))

@login_required
def CreateSubContainer(request):
    if request.method == 'POST':
        name = request.POST.get('name') if request.POST.get('name') else "Ninguno"
        container_id = int(request.POST.get('container_id'))
        obj = SubContainer.objects.filter(name=name, container_id=container_id).first()
        if not obj:
            obj = SubContainer(
                name = name,
                photo = request.FILES.get('photo'),
                container_id = container_id,
            )
            obj.save()
    return redirect('myadmin:adminroom', int(request.POST.get('room_id')))