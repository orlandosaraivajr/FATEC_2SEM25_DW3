from django.urls import path
from . import views
from .views import FeriadoListCreateView, FeriadoDetailView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('',views.feriados),
    path('api/feriados/', views.listar_feriados_json, name='listar_json'),
    path('api/feriados_rest/', FeriadoListCreateView.as_view(), name='feriado_list_create'),
    path('api/feriados_rest/<int:pk>/', FeriadoDetailView.as_view(), name='feriado_detail'),
    path('api-token/', obtain_auth_token, name='api_token'),
]
