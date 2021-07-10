# Generated by Django 3.2.4 on 2021-07-10 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_financiera', '0004_transferencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('Deposito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_financiera.deposito')),
                ('Retiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_financiera.retiro')),
                ('Transferencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_financiera.transferencia')),
            ],
        ),
    ]