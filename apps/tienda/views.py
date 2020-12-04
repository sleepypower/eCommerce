from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group
from apps.tienda.models import Usuario, Juego, Idioma 
from apps.tienda.forms import UsuarioForm, JuegoForm
from django.contrib.auth import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.shortcuts import redirect


@login_required
def sesion(request):
    if request.user.groups.filter(name='Cliente').exists():
        return render(request, 'tienda/portadaCliente.html')
    else:
        return render(request, 'tienda/portadaAdmin.html')

@staff_member_required
def crearUsuario(request):
     if request.method == 'POST':
          form = UsuarioForm(request.POST)
          form.save()
     else:
          form = UsuarioForm()
          return render(request, 'tienda/crearUsuario.html', {'form' : form})
@staff_member_required
def crearJuego(request):
     if request.method == 'POST':
          form = JuegoForm(request.POST)
          form.save()
     else:
          form = JuegoForm()
          return render(request, 'tienda/crearJuego.html', {'form' : form})
@staff_member_required
def consultarUsuario(request):
     usuarios = Usuario.objects.all()
     contexto = {'usuarios':usuarios}
     return render(request, 'tienda/consultarUsuario.html', contexto)
     
@login_required
def consultarJuego(request):
     juegos = Juego.objects.all()
     contexto = {'juegos':juegos}
     return render(request, 'tienda/consultarJuego.html', contexto)
@login_required
def consultarIdiomas(request):
     idiomas = Idioma.objects.all()
     contexto = {'idiomas':idiomas}
     return render(request, 'tienda/consultarIdiomas.html', contexto)
@staff_member_required
def consultarIdiomasA(request):
     idiomas = Idioma.objects.all()
     contexto = {'idiomas':idiomas}
     return render(request, 'tienda/consultarIdiomasA.html', contexto)
@staff_member_required
def consultarJuegoA(request):
     juegos = Juego.objects.all()
     contexto = {'juegos':juegos}
     return render(request, 'tienda/consultarJuegoA.html', contexto)    
def registro(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()
            group = Group.objects.get(name='Cliente')
            user.groups.add(group)
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('http://127.0.0.1:8000/tienda/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "tienda/registro.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
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
    return render(request, "tienda/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('http://127.0.0.1:8000/tienda/')


