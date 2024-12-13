from rest_framework import serializers
from .models import Rota, Ponto, Motorista, Mensagem

class PontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = ['id', 'referencia', 'latitude', 'longitude']

class RotaSerializer(serializers.ModelSerializer):
    # pontos = serializers.StringRelatedField(many=True)
    pontos = PontoSerializer(many=True, read_only=True)
    class Meta:
        model = Rota
        fields = ['id', 'nome', 'pontos']

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = ['motorista_id', 'descricao', 'estado', 'timestamp']

class MotoristaSerializer(serializers.ModelSerializer):
    mensagens = MensagemSerializer(many=True, read_only=True)
    class Meta:
        model = Motorista
        fields = ['matricula', 'nome', 'rota_id', 'latitude', 'longitude', 'timestamp', 'mensagens']
