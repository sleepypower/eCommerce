from django import forms
from apps.tienda.models import Usuario, Juego, Idioma

class UsuarioForm(forms.ModelForm):
    
 class Meta:
    model = Usuario
    fields = [
    'id_usuario'
    'Correo',
    'Nickname',
    'Clave',
    'Nombre',
    'Apellido',
    'Estado',
    'id_idioma'
    ]

    fields = {
    'id_usuario' : 'ID',
    'Correo' : 'Correo',
    'Nickname' : 'Nickname',
    'Nombre' : 'Nombre',
    'Apellido' : 'Apellido',
    'Estado' : 'Estado',
    'id_idioma' : 'id_idioma',
    'Clave' : 'Clave'
    }
    widgets = {
    'id_usuario': forms.TextInput(),
    'Correo': forms.TextInput(),
    'Nickname': forms.TextInput(),
    'Clave' : forms.TextInput(),
    'Nombre' : forms.TextInput(),
    'Apellido' : forms.TextInput(),
    'Estado' : forms.TextInput(),
    'Clave' : forms.TextInput()
    }

class JuegoForm(forms.ModelForm):
 class Meta:
      model = Juego
      fields = [
      'id_juego',
      'Titulo',
      'Fecha_Publicacion',
      'Precio',
      ]

      fields = {
      'id_juego' : 'id_juego',
      'Titulo' : 'Titulo',
      'Fecha_Publicacion' : 'Fecha_Publicacion',
      'Precio' : 'Precio',
      }
      widgets = {
      'id_juego': forms.TextInput(),
      'Titulo': forms.TextInput(),
      'Fecha_Publicacion' : forms.DateInput(),
      'Precio' : forms.TextInput(),
      }

