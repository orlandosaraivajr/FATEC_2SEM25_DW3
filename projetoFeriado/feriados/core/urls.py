from django.urls import path
from . import views
from .views import FeriadoListCreateView, FeriadoDetailView


urlpatterns = [
    path('',views.feriados),
    path('api/feriados/', views.listar_feriados_json, name='listar_json'),
    path('api/feriados_rest/', FeriadoListCreateView.as_view(), name='feriado_list_create'),
    path('api/feriados_rest/<int:pk>/', FeriadoDetailView.as_view(), name='feriado_detail'),
]
