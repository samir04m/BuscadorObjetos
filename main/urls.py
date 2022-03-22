from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('ingresar/', views.Igresar, name='ingresar'),
    path('login/<str:username>', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    
    path('objeto/<int:id>', views.Details, name='details'),
    path('busquedas/', views.MySearches, name='searches'),
]