from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('historial/', views.listado_gastos, name='listado_gastos'),
    path('nuevo/', views.formulario_gasto, name='formulario_gasto'),
]