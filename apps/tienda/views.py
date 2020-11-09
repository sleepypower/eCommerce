from django.shortcuts import render
from django.http import HttpResponse
from apps.tienda.models import Usuario, Juego, Idioma
from apps.tienda.forms import UsuarioForm, JuegoForm

def index(request):
    return render(request, 'tienda/inicio.html')


def crearUsuario(request):
     if request.method == 'POST':
          form = UsuarioForm(request.POST)
          form.save()
     else:
          form = UsuarioForm()
          return render(request, 'tienda/crearUsuario.html', {'form' : form})

def crearJuego(request):
     if request.method == 'POST':
          form = JuegoForm(request.POST)
          form.save()
     else:
          form = JuegoForm()
          return render(request, 'tienda/crearJuego.html', {'form' : form})

def consultarUsuario(request):
     usuarios = Usuario.objects.all()
     contexto = {'usuarios':usuarios}
     return render(request, 'tienda/consultarUsuario.html', contexto)
     

def consultarJuego(request):
     juegos = Juego.objects.all()
     contexto = {'juegos':juegos}
     return render(request, 'tienda/consultarJuego.html', contexto)

def consultarIdiomas(request):
     idiomas = Idioma.objects.all()
     contexto = {'idiomas':idiomas}
     return render(request, 'tienda/consultarIdiomas.html', contexto)
