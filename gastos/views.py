from django.shortcuts import render, redirect
from .models import Gasto

def landing(request):
    return render(request, 'gastos/landing.html')

def formulario(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        if descripcion and monto:
            Gasto.objects.create(descripcion=descripcion, monto=monto)
            return redirect('/')
    return render(request, 'gastos/formulario.html')

def listado(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    return render(request, 'gastos/listado.html', {'gastos': gastos})