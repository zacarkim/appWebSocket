from django.contrib import admin
from .models import Rota, Ponto, Motorista, Mensagem

class RotaAdmin(admin.ModelAdmin):
    pass #implementar conforme quer que apareça no admin

class PontoAdmin(admin.ModelAdmin):
    pass

class MotoristaAdmin(admin.ModelAdmin):
    pass

class MensagemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rota, RotaAdmin)
admin.site.register(Ponto, PontoAdmin)
admin.site.register(Motorista, MotoristaAdmin)
admin.site.register(Mensagem, MensagemAdmin)
