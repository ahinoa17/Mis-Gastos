from django.shortcuts import render, redirect
from .models import Gasto
from django.utils import timezone

def landing(request):
    return render(request, 'gastos/landing.html')

def formulario(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        if descripcion and monto:
            try:
                monto_float = float(monto)
                if monto_float > 0:
                    Gasto.objects.create(
                        descripcion=descripcion,
                        monto=monto_float,
                        fecha=timezone.now()
                    )
                    return redirect('/gastos/')
            except ValueError:
                pass  # El monto no es válido
    return render(request, 'gastos/formulario.html')

def listado(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    total_gastado = sum(gasto.monto for gasto in gastos)
    return render(request, 'gastos/listado.html', {
        'gastos': gastos,
        'total_gastado': "{:.2f}".format(total_gastado)
    })