# Generated by Django 3.2.4 on 2021-07-09 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_financiera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('monto_depositado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
