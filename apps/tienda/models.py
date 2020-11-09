from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(unique = True, null = False, primary_key = True)
    Correo = models.CharField(unique = True, max_length = 100)
    Nickname = models.CharField(max_length=100, unique = True, null = False)
    Clave = models.CharField(max_length=100, null = False)
    Nombre = models.CharField(max_length=45, null = False)
    Apellido = models.CharField(max_length=45, null = False)
    Estado = models.CharField(max_length=45)
    id_idioma = models.ForeignKey("Idioma", on_delete=models.CASCADE)

class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key = True)
    Nombre = models.CharField(max_length = 45, null = False)
    #Idioma_Juego = models.ForeignKey("Juego", on_delete=models.CASCADE)
    
class Categoria(models.Model):
    id = models.AutoField(primary_key= True)
    Nombre = models.CharField(max_length = 45, null = False)

class juegos_tiene_categorias(models.Model):
    #id_juego = models.ForeignKey("Juego", on_delete = models.CASCADE, primary_key = True)
    #id_categoria = models.ForeignKey("Categoria", on_delete = models.CASCADE, primary_key = True)
    id_juego = models.OneToOneField("Juego" , on_delete=models.CASCADE, primary_key=True)
    id_categoria = models.OneToOneField("Categoria" , on_delete=models.CASCADE)


class Developer(models.Model):
    id_developer = models.AutoField(primary_key = True)
    Nombre = models.CharField(max_length = 45, null = False)

class juegos_tiene_developers(models.Model):
    #id_juego = models.ForeignKey("Juego", on_delete = models.CASCADE, primary_key = True)
    #id_developer = models.ForeignKey("Developer", on_delete = models.CASCADE, primary_key = True)
    id_juego = models.OneToOneField("Juego" , on_delete=models.CASCADE, primary_key=True)
    id_developer = models.OneToOneField("Developer" , on_delete=models.CASCADE)

class Resena(models.Model):
    id_resena = models.IntegerField(primary_key= True)
    Texto = models.TextField()
    Correo = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    id_valoracion = models.ForeignKey("Valoracion", on_delete=models.CASCADE)
    id_juego = models.ForeignKey("Juego", on_delete=models.CASCADE)

class Valoracion(models.Model):
    id_valoracion = models.AutoField(primary_key = True)
    Texto = models.CharField(max_length=20, null = False)
    #Correo_Usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

"""
class Carrito(models.Model):
    id = models.IntegerField(primary_key= True)
    Precio_total = models.IntegerField()
    id_juego = models.ForeignKey("Juego", on_delete=models.CASCADE)
    Correo_Usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
"""

class Factura(models.Model):
    id_factura = models.AutoField(primary_key= True)
    valor_Total = models.FloatField(null=False)
    fecha = models.DateField(null=False)
    correo = models.ForeignKey("Usuario", on_delete=models.CASCADE)


class Juego(models.Model):
    id_juego = models.AutoField(primary_key = True)
    Titulo = models.CharField(max_length = 45, null=False)
    Fecha_Publicacion = models.DateField()
    Precio = models.FloatField()
    #idDev = models.ForeignKey("Desarrollador", on_delete=models.CASCADE)
    #idIdioma = models.ForeignKey("Idioma",on_delete=models.CASCADE)
    #idReview = models.ForeignKey("Review",on_delete=models.CASCADE)

class juegos_tiene_idiomas(models.Model):
    #id_juego = models.ForeignKey("Juego", on_delete = models.CASCADE, primary_key = True)
    #id_idioma = models.ForeignKey("Idioma", on_delete = models.CASCADE, primary_key = True)
    id_juego = models.OneToOneField("Juego" , on_delete=models.CASCADE, primary_key=True)
    id_idioma = models.OneToOneField("Idioma" , on_delete=models.CASCADE)
    

class Factura_juego(models.Model):
    id_factura_producto = models.AutoField(primary_key = True)
    Cantidad = models.IntegerField(null=False)
    Valor = models.FloatField(null=False)
    id_juego = models.ForeignKey("Juego", on_delete = models.CASCADE)
    id_factura = models.ForeignKey("Factura", on_delete = models.CASCADE)


