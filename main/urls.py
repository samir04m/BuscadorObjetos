from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.Home, name='home'),
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.Logout, name='logout'),
    
    path('objeto/<int:id>', views.Details, name='details'),
    path('busquedas/', views.MySearches, name='searches'),
]