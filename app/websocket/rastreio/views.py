from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Rota, Motorista
from .serializers import RotaSerializer, MotoristaSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class RotaViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def obter_rotas(self, request):
        # carro_id = request.query_params.get('carro_id')
        # if not carro_id:
        #     return Response({"erro": "carro_id é necessário"}, status=400)
        
        # localizacao = get_object_or_404(Localizacao, carro_id=carro_id)

        
        rotas = Rota.objects.all()
        serializer = RotaSerializer(rotas, many=True)
        return Response(serializer.data)
    
class MotoristaViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def obter_rastreio(self, request):        
        rastreio = Motorista.objects.all()
        serializer = MotoristaSerializer(rastreio, many=True)
        return Response(serializer.data)

