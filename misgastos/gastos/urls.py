from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('formulario/', views.formulario, name='formulario'),
    path('gastos/', views.listado, name='listado'),
]