from django.urls import path
from apps.tienda.views import index, crearUsuario, consultarUsuario,crearJuego, consultarJuego, consultarIdiomas

urlpatterns = [
    path('',index),
    path('crearUsuario/', crearUsuario),
    path('consultarUsuario/', consultarUsuario),
    path('crearJuego/', crearJuego),
    path('consultarIdiomas/', consultarIdiomas),
    path('consultarJuego/', consultarJuego),
]