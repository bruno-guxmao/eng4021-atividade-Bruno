from django.contrib import admin
from .models import Task

admin.site.register(Task) # Registra o modelo Task no painel de administração do Django
