from django.contrib import admin
from .models import Usuario

# Register your models here.
from .models import Rol, Usuario, Opinion, Encuesta, Pregunta, Respuesta, Alternativa

# Registra tus modelos aquí
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Opinion)
admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Alternativa)