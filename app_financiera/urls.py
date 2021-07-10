from django.urls import path
from . import views

app_name = 'fina'

urlpatterns = [
    path('', views.index, name="index"),
    path('deposito/', views.deposito, name="deposito"),
    path('retiro/', views.retiro, name="retiro"),
    path('transferencia/', views.transferencia, name="transferencia"),
]