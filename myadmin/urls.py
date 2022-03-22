from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdminHome, name='adminhome'),  
    path('room/<int:id>/', views.AdminRoom, name='adminroom'),
    path('object/create/<int:id>', views.CreateObject, name='createobject'),
]