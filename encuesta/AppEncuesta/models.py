import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Rol(models.Model):
    nombre_rol = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre_rol

class Usuario(AbstractUser):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=255)
    numero_telefonico = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    nombre_empresa = models.CharField(max_length=255)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE,default = "COLABORADOR")
   
   #modificado
    def __str__(self):
        return self.username
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )
    

class Opinion(models.Model):
    rut = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    asunto=models.CharField(max_length=55)
    texto = models.TextField()
    clasificacion = models.SmallIntegerField(choices=[(1, 'supersatisfecho'), (2, 'satisfecho'), (3, 'insatisfecho')])# ver si puede ser ,supersatisfecho, satisfecho,insatisfecho 
    fecha = models.DateField(default=datetime.datetime.now())

class Encuesta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(null=True, blank=True)
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
    

class Pregunta(models.Model):
    tipo_pregunta = models.SmallIntegerField(choices=[(1, '1'), (2, '2')])
    id_encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    pregunta_texto = models.TextField()
    def __str__(self):
        return self.pregunta_texto
    
class Alternativa(models.Model):
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_alternativa = models.CharField(max_length=255)
    def __str__(self):
        return self.texto_alternativa


class Respuesta(models.Model):
    tipo_respuesta = models.CharField(max_length=255)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_texto = models.TextField()
    def __str__(self):
        return self.respuesta_texto
    
class RespuestaAlternativa(models.Model):
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.id_alternativa.texto_alternativa