from django.urls import path
from .views import RotaViewSet, MotoristaViewSet

rota_list = RotaViewSet.as_view({'get': 'obter_rotas'})
rastreio_list = MotoristaViewSet.as_view({'get': 'obter_rastreio'})

urlpatterns = [
    path('api/rotas/', rota_list, name='obter_rotas'),
    path('api/rastreio/', rastreio_list, name='obter_rastreio'),
]
