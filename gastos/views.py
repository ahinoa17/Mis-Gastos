from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Gasto
from django.utils.timezone import now

def landing(request):
    total_gastado = Gasto.objects.aggregate(Sum('monto'))['monto__sum'] or 0
    gastos_count = Gasto.objects.count()
    return render(request, 'gastos/landing.html', {
        'total_gastado': total_gastado,
        'gastos_count': gastos_count,
        'now': now(),
    })

def listado_gastos(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    total_gastado = Gasto.objects.aggregate(Sum('monto'))['monto__sum'] or 0
    return render(request, 'gastos/listado.html', {
        'gastos': gastos,
        'total_gastado': total_gastado,
        'now': now(),
    })

def formulario_gasto(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        if descripcion and monto:
            try:
                monto = float(monto)
                if monto > 0:
                    Gasto.objects.create(descripcion=descripcion, monto=monto)
                    return redirect('listado_gastos')
            except ValueError:
                pass
    return render(request, 'gastos/formulario.html', {'now': now()})