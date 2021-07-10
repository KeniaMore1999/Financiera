from django.contrib import admin
from app_financiera.models import Cliente, CuentaBancaria, Transacciones

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion','fecha_nacimiento','telefono','correo')

class CuentaAdmin(admin.ModelAdmin):
    list_display = ('fecha_creacion', 'estado', 'saldo','propietario')  

class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido') 

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(CuentaBancaria, CuentaAdmin)
admin.site.register(Transacciones, TransaccionAdmin)
