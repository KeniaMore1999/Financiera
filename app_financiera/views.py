from django.shortcuts import render
from .models import Deposito, Retiro, Transferencia

# Create your views here.
def index(request):
    return render(request, 'app_financiera/index.html')

def deposito(request):
    if request.method == 'POST':
        nombre  = request.POST.get('nombre')
        apellido  = request.POST.get('apellido')
        monto_depositado = request.POST.get('monto_depositado')

        p = Deposito(
            nombre = nombre, 
            apellido = apellido, 
            monto_depositado = monto_depositado
            )
        p.save()
        
    activo= 'deposito'

    data = Deposito.objects.all().order_by('nombre')

    ctx = {
        'activo':activo,
        'formulario': data
    }

    return render(request, 'app_financiera/depositos.html', ctx)
    

def retiro(request):
    if request.method == 'POST':
        nombre  = request.POST.get('nombre')
        apellido  = request.POST.get('apellido')
        monto_retirado = request.POST.get('monto_retirado')
        monto = request.POST.get('monto')

        p = Retiro(
            nombre = nombre, 
            apellido = apellido, 
            monto_retirado = monto_retirado,
            monto = monto
            )
        p.save()
        
    activo= 'deposito'

    data = Retiro.objects.all().order_by('nombre')

    ctx = {
        'activo':activo,
        'formulario': data
    }

    return render(request, 'app_financiera/retiros.html', ctx)

def transferencia(request):
    if request.method == 'POST':
        cuenta_origen  = request.POST.get('cuenta_origen')
        cuenta_destino  = request.POST.get('cuenta_destino')
        monto_depositar = request.POST.get('monto_depositar')
        descripcion_trasferencia = request.POST.get('descripcion_transferencia')

        p = Transferencia(
            cuenta_origen = cuenta_origen, 
            cuenta_destino = cuenta_destino, 
            monto_depositar = monto_depositar,
            descripcion_trasferencia = descripcion_trasferencia
            )
        p.save()
        
    activo= 'transferencia'

    data = Transferencia.objects.all().order_by('cuenta_origen')

    ctx = {
        'activo':activo,
        'formulario': data
    }

    return render(request, 'app_financiera/transferencias.html', ctx)