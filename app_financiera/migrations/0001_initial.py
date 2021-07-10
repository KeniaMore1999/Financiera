# Generated by Django 3.2.4 on 2021-07-09 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.TextField()),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaBancaria',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('1', 'Activa'), ('2', 'Inactiva')], default='1', max_length=1)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('propietario', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app_financiera.cliente')),
            ],
        ),
    ]
