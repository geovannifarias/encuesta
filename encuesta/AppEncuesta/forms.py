from django import forms
from AppEncuesta.models import *
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    rut = forms.CharField(label='RUT', required=True, max_length=10,
                          widget=forms.TextInput(attrs={
                              'class': 'form-control',
                              'placeholder': 'RUT'
                          }))
    nombre = forms.CharField(label='Nombres', required=True, min_length=4, max_length=60,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Nombre'
                             }))
    apellido = forms.CharField(label='Apellidos', required=True, min_length=4, max_length=60,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Apellidos'
                               }))
    numero_telefonico = forms.CharField(label='Número Telefónico', required=True, max_length=20,
                                        widget=forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Número Telefónico'
                                        }))
    email = forms.EmailField(label='Correo Electrónico', required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'ejemplo@empresa.cl'
                             }))
    nombre_empresa = forms.CharField(label='Nombre de la Empresa', required=True, max_length=255,
                                     widget=forms.TextInput(attrs={
                                         'class': 'form-control',
                                         'placeholder': 'Nombre de la Empresa'
                                     }))

    password1 = forms.CharField(label='Contraseña', required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Contraseña'
                               }))
    password2 = forms.CharField(label='Repetir Constraseña',required=True,
                                widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Repetir Contraseña'
                               }))

    class Meta:
        model = Usuario
        fields = ['rut', 'username', 'nombre', 'apellido', 'email', 'numero_telefonico', 'nombre_empresa','id_rol']

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        # Agrega lógica de validación para el RUT si es necesario
        return rut
    def guardarUsuario(self):
        return Usuario.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name')
        )
    

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['asunto','texto', 'clasificacion']
        widgets = {
            'asunto': forms.TextInput(attrs= {'class':'form-control'} ),   
            'clasificacion': forms.Select(attrs= {'class':'form-control'} ),
            
        }

        

class AlternativaForm(forms.ModelForm):
    class Meta:
        model = Alternativa
        fields = '__all__'
        widgets = {
            'id_pregunta': forms.Select(attrs= {'class':'form-control'} ),
            'texto_alternativa': forms.TextInput(attrs= {'class':'form-control'} ),  #text input es referencia a los charfield '': forms.TextInput(attrs= {'class':'form-control'} ),  
        }

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'descripcion']
    
    # Nuevo campo para el rut_usuario
    rut_usuario_manual = forms.CharField(max_length=10, required=True)


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['tipo_pregunta', 'id_encuesta', 'pregunta_texto']
