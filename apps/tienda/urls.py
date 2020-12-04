from django.urls import path
from apps.tienda.views import  crearUsuario, \
    consultarUsuario,crearJuego, consultarJuego, consultarIdiomas, registro, login, logout, sesion, consultarJuegoA, consultarIdiomasA

urlpatterns = [
    path('',sesion),
    path('crearUsuario/', crearUsuario),
    path('consultarUsuario/', consultarUsuario),
    path('crearJuego/', crearJuego),
    path('consultarIdioma/', consultarIdiomas),
    path('consultarIdiomasA/', consultarIdiomasA),
    path('consultarJuego/', consultarJuego),
    path('consultarJuegoA/', consultarJuegoA),
    path('registro', registro),
    path('login', login),
    path('logout', logout)

]