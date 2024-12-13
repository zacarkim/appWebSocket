from django.db import models

class Rota(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)   

    def __str__(self):
        return f"Rota {self.id} - Nome: {self.nome}"
    
class Ponto(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=100)
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    rota_id = models.ForeignKey(Rota, related_name='pontos', on_delete=models.CASCADE)    

    def __str__(self):
        return f"Ponto {self.referencia} - Lat: {self.latitude}, Lng: {self.longitude}"

class Motorista(models.Model):
    matricula = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=100)
    rota_id = models.ForeignKey(Rota, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Motorista {self.nome} - Rota: {self.rota_id}, Data: {self.timestamp}, Lat: {self.latitude}, Lng: {self.longitude}"

class Mensagem(models.Model):
    motorista_id = models.ForeignKey(Motorista, related_name='mensagens', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Motorista {self.motorista_id} - Mensagem: {self.descricao}, Data: {self.timestamp}"

