from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
    path('<str:isbn>/', views.libro_detalle, name='libro_detalle'),
]