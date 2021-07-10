from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    correo = models.EmailField(null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CuentaBancaria(models.Model):
    ESTADOS=(
        ('1', 'Activa'),
        ('2', 'Inactiva')
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='1')
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    propietario = models.OneToOneField(Cliente, blank=True, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return self.estado

class Deposito(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    monto_depositado = models.DecimalField(max_digits=10, decimal_places=2)
    

class Retiro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    monto_retirado = models.DecimalField(max_digits=10, decimal_places=2)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def monto_total(self):
        monto_final = self.cuentabancaria_set.count()
        return self.monto - monto_final #con self accedemos a los campos 

class Transferencia(models.Model):
    cuenta_origen = models.CharField(max_length=40)
    cuenta_destino = models.CharField(max_length=40)
    fecha_transferencia = models.DateTimeField(auto_now_add=True)
    monto_depositar = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_transferencia = models.TextField()

    def __str__(self):
        return self.cuenta_destino

class Transacciones(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE)
    retiro = models.ForeignKey(Retiro, on_delete=models.CASCADE)
    transferencia = models.ForeignKey(Transferencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

