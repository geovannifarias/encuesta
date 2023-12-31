import datetime
from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .models import RespuestaAlternativa, Usuario, Encuesta, Pregunta, Alternativa
from .forms import RegistroForm, AlternativaForm , AlternativaForm, EncuestaForm, PreguntaForm # Asegúrate de importar el formulario
from django.http import JsonResponse
from django.contrib import messages
from .forms import OpinionForm
from .models import Opinion
from AppEncuesta import models

# Create your views here.


def inicio(request):    
    return render(request, 'TemplatesEncuesta/inicio.html')

def rrhh(request):

    return render(request, 'TemplatesEncuesta/rrhh.html')

def listado_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'TemplatesEncuesta/rrhh.html', {'mostrar': usuarios})

def start(request):

    return render(request, 'TemplatesEncuesta/start.html')


#--------------visualizar de la encuesta-------------------------

def encuesta(request):
    encuestas = Encuesta.objects.all()
    #preguntas = Pregunta.objects.all()
    return render(request, 'TemplatesEncuesta/encuesta.html', {
        'encuestas': encuestas,
        #'preguntas': preguntas
    })

def pregunta(request, id):
    encuestas = Encuesta.objects.get(id=id)
    preguntas = Pregunta.objects.filter(id_encuesta = encuestas)

    return render(request, 'TemplatesEncuesta/preguntas.html', {
        'preguntas': preguntas,
    })


#----------agregar encuesta ------------

def agregar_encuesta(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            nueva_encuesta = form.save(commit=False)
            
            # Asegúrate de obtener un objeto Usuario válido antes de asignarlo
            # a rut_usuario.
            rut_usuario_manual = form.cleaned_data['rut_usuario_manual']
            usuario = Usuario.objects.get(rut=rut_usuario_manual)
            nueva_encuesta.rut_usuario = usuario
            
            nueva_encuesta.save()
            return redirect('../agregar_pregunta/')

    else:
        form = EncuestaForm()

    return render(request, 'TemplatesEncuesta/agregarEncuesta.html', {
        'form': form
    })



#-----------------agregar alternativa----------------
def agregar_alternativa(request):
    if request.method == 'POST':
        form = AlternativaForm(request.POST)
        if form.is_valid():
            nueva_alternativa = form.save(commit=False)
            nueva_alternativa.pregunta = encuesta
            nueva_alternativa.save()
            #return redirect(pregunta)
    else:
        form = AlternativaForm()

    return render(request, 'TemplatesEncuesta/alternativa.html', {
    'form': form
    })



#---------------Agregar pregunta------------------

def agregar_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            nueva_pregunta = form.save()
            # Puedes redirigir a la página que desees, por ejemplo, la página de la encuesta
            return redirect('../alternativa/')
    else:
        form = PreguntaForm()

    return render(request, 'TemplatesEncuesta/crearPreguntas.html', {
        'form': form,
    })


#-------------------agregar------------------

def registro_usuario(request):
    formAdd = RegistroForm()

    if request.method == 'POST':
        formAdd = RegistroForm(request.POST)
        if formAdd.is_valid():
            formAdd.save()
            # Puedes redirigir a donde desees después de agregar un usuario
            return redirect(listado_usuarios)

    data = {'formAdd': formAdd}
    return render(request, 'TemplatesEncuesta/agregar.html', data)

#----------login------------------

def Login(request):
    # Redirección en caso de que exista una sesión activa
    username = request.session.get('user')
    password = request.session.get('clave')
    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.id_rol.nombre_rol == 'RRHH':
                    return render(request, 'TemplatesEncuesta/inicio.html', {})
            elif user.id_rol.nombre_rol == 'COLABORADOR':
                return render(request, 'TemplatesEncuesta/start.html', {})

    # Si no existe una sesión activa, se procede a realizar el login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        txt = "username: {0} y password: {1}"
        # print(txt.format(username, password))
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            request.session['user'] = username
            request.session['clave'] = password
            # print(user.id_rol.nombre_rol)
            # Redirige según el rol
            if user.id_rol.nombre_rol == 'RRHH':
                return render(request, 'TemplatesEncuesta/inicio.html', {})
            elif user.id_rol.nombre_rol == 'COLABORADOR':
                return render(request, 'TemplatesEncuesta/start.html', {})

            # Agrega otros roles según sea necesario
        else:
            if username is None and password is None:
                pass
            else:
                messages.error(request, 'Usuario o Contraseña incorrectos')

    return render(request, 'TemplatesEncuesta/login.html', {})

def logout(request):
    request.session.flush()
    return redirect('login')


#------------------editar-------------
def editar(request,rut):
    User = Usuario.objects.get(rut = rut)
    formUser = RegistroForm(instance= User)
    if request.method == 'POST':
        formUser= RegistroForm(request.POST,instance= User)
        if formUser.is_valid():
            formUser.save()
            return redirect(listado_usuarios)
        
    data= {'formUser':formUser}     

    return render(request, 'TemplatesEncuesta/editar.html',data)

def eliminar (request,rut):
    delete = Usuario.objects.get(rut = rut)
    delete.delete()
    return redirect (listado_usuarios)


#--------opinion--------
def opinion(request):
    if request.method == 'POST':
        formAddOpinion = OpinionForm(request.POST)
        if formAddOpinion.is_valid():
            rut = request.user
            print(formAddOpinion.cleaned_data)
            newOpinion = models.Opinion(rut = rut, asunto = formAddOpinion.data.get ("asunto"),texto = formAddOpinion.data.get("texto"),clasificacion = formAddOpinion.data.get("clasificacion"))
            newOpinion.save()
            formAddOpinion.data.get("asunto")
            # Redirige a la vista mostrar_opinion con el rut del usuario asociado a la opinión
            return redirect('mostrar_opinion', rut=newOpinion.rut)
    
    else:
        formAddOpinion = OpinionForm()

    data = {'formAddOpinion': formAddOpinion}
    return render(request, 'TemplatesEncuesta/opinion.html', data)


def mostrar_opinion(request, rut):
    opinion = Opinion.objects.all()
    return render(request, 'TemplatesEncuesta/mostrar_opinion.html', {'mostrar': opinion})


#---- Ver encuestas disponibles para responder ----
def ver_encuestas(request):
    encuestas = Encuesta.objects.all()
    return render(request, 'TemplatesEncuesta/ver_encuestas.html', {'encuestas': encuestas})

#---- Responder encuesta ----
def responder_encuesta(request, id):
    if request.method == 'GET':
        encuesta = Encuesta.objects.get(id=id)
        preguntas = Pregunta.objects.filter(id_encuesta = encuesta)
        print(preguntas)
        alternativas = Alternativa.objects.filter(id_pregunta__in=preguntas)
        print(alternativas)
        return render(request, 'TemplatesEncuesta/responder_encuesta.html', {
            'encuesta': encuesta,
            'preguntas': preguntas,
            'alternativas': alternativas,
        })
    if request.method == 'POST':
        # print(request.POST)
        # Obtener usuario
        usuario  = request.user
        # Obtener preguntas
        preguntas = Pregunta.objects.filter(id_encuesta__id=id)
        # Obtener respuestas
        respuestas = []
        for pregunta in preguntas:
            # Obtener respuesta
            respuesta = request.POST.get('pregunta-' + str(pregunta.id))
            # Si la respuesta es una alternativa
            if respuesta is not None:
                # Crear respuesta alternativa
                respuesta = RespuestaAlternativa(
                    id_usuario=usuario,
                    id_pregunta=pregunta,
                    id_alternativa=Alternativa.objects.get(id=respuesta)
                )
                respuesta.save()

        
        return ver_encuestas(request)
    
# Resultados encuestas
def resultados_encuestas(request):
    respuestas = RespuestaAlternativa.objects.all()
    # Agrupar por pregunta
    encuestas  = {}
    for respuesta in respuestas:
        # Si no está la encuesta se agregan los diccionarios
        if respuesta.id_pregunta.id_encuesta not in encuestas:
            encuestas[respuesta.id_pregunta.id_encuesta] = {}

        # Si no está la pregunta se agregan los diccionarios
        if respuesta.id_pregunta not in encuestas[respuesta.id_pregunta.id_encuesta]:
            encuestas[respuesta.id_pregunta.id_encuesta][respuesta.id_pregunta] = {}

        # Si no está la alternativa se agregan los diccionarios
        if respuesta.id_alternativa not in encuestas[respuesta.id_pregunta.id_encuesta][respuesta.id_pregunta]:
            encuestas[respuesta.id_pregunta.id_encuesta][respuesta.id_pregunta][respuesta.id_alternativa] = 0

        # Se suma 1 a la alternativa
        encuestas[respuesta.id_pregunta.id_encuesta][respuesta.id_pregunta][respuesta.id_alternativa] += 1
    
    # Agregar ceros a alternativas sin respuestas
    for encuesta in encuestas:
        for pregunta in encuestas[encuesta]:
            for alternativa in Alternativa.objects.filter(id_pregunta=pregunta.id):
                if alternativa not in encuestas[encuesta][pregunta]:
                    encuestas[encuesta][pregunta][alternativa] = 0
    return render(request, 'TemplatesEncuesta/resultados_encuestas.html', {'encuestas': encuestas})
