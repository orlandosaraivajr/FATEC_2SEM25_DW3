from django.urls import path
from . import views

urlpatterns = [
    path('',views.feriados),
    path('api/feriados/', views.listar_feriados_json, name='listar_json'),
]
