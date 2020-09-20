from . import views
from django.urls import path

app_name = 'relatorio'

urlpatterns = [
   path('', views.relatorio, name='relatorio'),
   path('filtro/', views.relatorio_filtro, name='filtro'),
]
