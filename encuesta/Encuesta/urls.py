"""
URL configuration for Encuesta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppEncuesta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login, name='login'),
    path('rrhh/', views.listado_usuarios, name='listado_usuarios'),# esta es donde aparece las tablas
    path('inicio/', views.inicio, name='inicio'),
    path('agregar/', views.registro_usuario, name='agregar'),
    path('editar/<str:rut>/', views.editar, name="editar"),
    path('eliminar/<str:rut>/',views.eliminar, name="eliminar"),
    path('start/', views.start, name='start'),
    path('opinion/', views.opinion, name='opinion'),
    path('mostrar_opinion/<str:rut>/', views.mostrar_opinion, name='mostrar_opinion'),
    path('encuesta/', views.encuesta, name='encuesta'),#1
    path('pregunta/<int:id>/', views.pregunta, name='pregunta'),
    path('alternativa/', views.agregar_alternativa, name='alternativa'),
    path('crear_encuesta/', views.agregar_encuesta, name='agregar encuesta'),
    path('agregar_pregunta/', views.agregar_pregunta, name='agregar pregunta'),
    path('ver_encuestas/', views.ver_encuestas, name='ver encuestas'),
    path('responder_encuesta/<int:id>/', views.responder_encuesta, name='responder encuesta'),
    path('logout/', views.logout, name='logout'),
    path('resultados_encuestas', views.resultados_encuestas, name='resultados_encuestas'),

]
