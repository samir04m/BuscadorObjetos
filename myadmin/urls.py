from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdminHome, name='adminhome'),  
    path('room/<int:id>/', views.AdminRoom, name='adminroom'),
    path('subcontainer/<int:id>', views.AdminSubcontainer, name='adminsubcontainer'),
    path('object/create/', views.CreateObject, name='createobject'),
    path('room/create/', views.CreateRoom, name='createroom'),
    path('container/create/', views.CreateContainer, name='createcontainer'),
    path('subcontainer/create/', views.CreateSubcontainer, name='createsubcontainer'),
]