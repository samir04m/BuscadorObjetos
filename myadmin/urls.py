from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdminHome, name='adminhome'),  
    path('room/<int:id>/', views.AdminRoom, name='adminroom'),
    path('subcontainer/<int:id>', views.AdminSubcontainer, name='adminsubcontainer'),
    path('object/create/', views.CreateObject, name='createobject'),
]