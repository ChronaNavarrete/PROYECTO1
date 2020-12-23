from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

#post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, PostView, Like, Comment, User, Profile
from posts.forms import PostForm, CommentForm

#users
from users.forms import CreateUserForm, LoginForm, EditProfileForm

#cabildos
import json
from cabildos.forms import CrearCabildo
from cabildos.forms import Cabildo_OnlineForm
from cabildos.models import Cabildo_Online, Cabildo, get_conceptos_Valores, get_conceptos_Derechos, get_conceptos_Deberes, get_conceptos_Instituciones 


User = get_user_model

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "index.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def register(request, backend='django.contrib.auth.backends.ModelBackend'):
    # Creamos el formulario de autenticación vacío
    form = CreateUserForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = CreateUserForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = LoginForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = LoginForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance= request.user)

        if form.is_valid():
            form.save()
            return redirect('/perfil')
    else:
        form = EditProfileForm(instance= request.user)
        args = {'edit_form': form}
        return render(request, 'editar_perfil.html', args)



def calendario(request):
    return render(request, 'calendario.html')

def index(request):
    return render(request, 'index.html')

def cabildos(request):
    return render(request, 'cabildos.html')   #?

def perfil(request):
    return render(request, 'perfil.html')

def temas(request):
    return render(request, 'temas.html')

def Cabildo_OnlineView(request):
    if request.method == "POST" : 
        form = Cabildo_OnlineForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/calendario")
    else:
        form = Cabildo_OnlineForm()
    return render(request, "calendario.html", {"form" : form})

def cabildo(request):
    context = {}

    cabildo_form = CrearCabildo()
    context['cabildo_form'] = cabildo_form
    #context = {'form':form}

    conceptos_Valores = get_conceptos_Valores()
    conceptos_Derechos = get_conceptos_Derechos()
    conceptos_Deberes = get_conceptos_Deberes()
    conceptos_Instituciones = get_conceptos_Instituciones()

    json_conceptos_Valores = json.dumps(conceptos_Valores)
    json_conceptos_Derechos =json.dumps(conceptos_Derechos)
    json_conceptos_Deberes = json.dumps(conceptos_Deberes)
    json_conceptos_Instituciones = json.dumps(conceptos_Instituciones)

    context['json_conceptos_Valores'] = json_conceptos_Valores
    context['json_conceptos_Derechos'] = json_conceptos_Derechos
    context['json_conceptos_Deberes'] = json_conceptos_Deberes
    context['json_conceptos_Instituciones'] = json_conceptos_Instituciones

    if request.method == 'POST':
        form = CrearCabildo(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'cabildo.html', context)   

