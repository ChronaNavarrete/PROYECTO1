from django.db import models
from django.contrib.auth.models import AbstractUser , User
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify
from cabildos.models import Cabildo
from ckeditor.fields import RichTextField
# Create your models here.

class User(AbstractUser):
    pass
    #name = models.CharField(max_length=200)
    #email = models.EmailField()
    #password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.username)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

CATEGORIAS = (
        ('Valores', 'Valores'),
        ('Derechos', 'Derechos'),
        ('Deberes', 'Deberes'),
        ('Instituciones', 'Instituciones'),
    )

V_0 = "Valores Derechos"
V_1 = "Amistad civica"
V_2 = "Autonomia libertad"
V_3 = "Bien comun comunidad"
V_4 = "Buen vivir"
V_5 = "Ciudadania"
V_6 = "Democracia"
V_7 = "Desarrollo"
V_8 = "Desarrollo sustentable"
V_9 = "Descentralizacion"
V_10 = "Dignidad"
V_11 = "Diversidad"
V_12 = "Emprendimiento libre"
V_13 = "Equidad de gÃ©nero"
V_14 = "Estado de derecho"
V_15 = "Estado garante"
V_16 = "Estado laico"
V_17 = "Estado solidario"
V_18 = "Familia"
V_19 = "Felicidad"
V_20 = "Fraternidad"
V_21 = "Identidad cultural"
V_22 = "Igualdad"
V_23 = "Igualdad de oportunidades"
V_24 = "Inclusion"
V_25 = "Innovacion creatividad"
V_26 = "Integracion"
V_27 = "Justicia"
V_28 = "Justicia social"
V_29 = "Medio ambiente"
V_30 = "Multiculturalidad"
V_31 = "Participacion ciudadana"
V_32 = "Patriotismo"
V_33 = "Paz convivencia pacifica"
V_34 = "Pluralismo"
V_35 = "Plurinacionalismo"
V_36 = "Probidad"
V_37 = "Republica"
V_38 = "Respeto"
V_39 = "Respeto conservacion de la naturaleza o medio ambiente"
V_40 = "Seguridad"
V_41 = "Soberania"
V_42 = "Soberania popular"
V_43 = "Solidaridad"
V_44 = "Subsidiaridad"
V_45 = "Tolerancia"
V_46 = "Transparencia"
V_47 = "Transparencia y publicidad"
V_48 = "Unidad"


Der_0 = "A huelga"
Der_1 = "A la educacion"
Der_2 = "A la honra, al honor"
Der_3 = "A la identidad cultural"
Der_4 = "A la informacion"
Der_5 = "A la integracion de discapacidad"
Der_6 = "A la integridad fisica y psiquica"
Der_7 = "A la nacionalidad"
Der_8 = "A la participacion"
Der_9 = "A la salud"
Der_10 = "A la seguridad social"
Der_11 = "A la seguridad vida sin violencia"
Der_12 = "A la vida"
Der_13 = "A la vida digna"
Der_14 = "A la vivienda digna"
Der_15 = "A sindicalizarse y a la negociacion colectiva"
Der_16 = "A sufragio votar"
Der_17 = "Acceso a informacion publica"
Der_18 = "Acceso a la cultura"
Der_19 = "Al agua"
Der_20 = "Al salario equitativo"
Der_21 = "Al trabajo"
Der_22 = "Articulo 19"
Der_23 = "De los pueblos indigenas"
Der_24 = "De peticion ante las autoridades"
Der_25 = "De propiedad"
Der_26 = "Derecho al agua"
Der_27 = "Derecho de asociacion"
Der_28 = "Derechos del niño, niña y adolescente"
Der_29 = "Igualdad ante la ley"
Der_30 = "Igualdad ante las cargas publicas"
Der_31 = "Igualdad ante los tributos"
Der_32 = "Igualdad de acceso a la justicia debido proceso"
Der_33 = "Igualdad de genero"
Der_34 = "Jubilacion digna"
Der_35 = "Libertad ambulatoria"
Der_36 = "Libertad de conciencia"
Der_37 = "Libertad de culto"
Der_38 = "Libertad de enseñanza"
Der_39 = "Libertad de expresion"
Der_40 = "Libertad de trabajo"
Der_41 = "Libertad personal"
Der_42 = "Libertad religiosa"
Der_43 = "Libre iniciativa economica, libre empresa"
Der_44 = "No discriminacion"
Der_45 = "Privacidad e intimidad"
Der_46 = "Proteccion judicial de los derechos"
Der_47 = "Respeto a la naturaleza medio ambiente"
Der_48 = "Reunion pacifica"
Der_49 = "Seguridad social"
Der_50 = "Ser elegido en cargos publicos"
Der_51 = "Sexuales y reproductivos"
Der_52 = "Trabajo digno"


Deb_0 = "Cumplimiento de las leyes y normas"
Deb_1 = "Cumplimiento de obligaciones fiscales"
Deb_2 = "Cumplimiento de tratados y obligaciones internacionales"
Deb_3 = "De proteccion y conservacion de patrimonio historico y cultural"
Deb_4 = "De satisfacer cargas publicas"
Deb_5 = "Deber de transparencia en los actos de gobierno"
Deb_6 = "Deberes de proteccion de conservacion de la naturaleza"
Deb_7 = "Educacion civica"
Deb_8 = "Ejercicio legitimo y no abusivo de los derechos"
Deb_9 = "Promocion de los derechos fundamentales"
Deb_10 = "Proteccion, promocion y respeto de los derechos humanos y fundamentales"
Deb_11 = "Respeto de derechos de otros"
Deb_12 = "Respeto por la constitucion"
Deb_13 = "Responsabilidad"
Deb_14 = "Responsabilidad civica"
Deb_15 = "Servicio a la comunidad"
Deb_16 = "Unidad nacional y respeto por chile"
Deb_17 = "Voto obligatorio"


I_0 = "Asamblea constituyente"
I_1 = "Banco central"
I_2 = "Cambio o reforma constitucional"
I_3 = "Congreso o parlamento, estructura y funciones"
I_4 = "Congreso unicameral"
I_5 = "Contraloria general tribunales de cuentas"
I_6 = "Defensor del pueblo ciudadano"
I_7 = "Division territorial"
I_8 = "Estado de excepcion"
I_9 = "Fiscalizacion"
I_10 = "Forma de estado, federalismo autonomias regionales"
I_11 = "Fuerzas armadas"
I_12 = "Gobierno local municipal"
I_13 = "Gobierno nacional estructura y funciones"
I_14 = "Gobierno provincial"
I_15 = "Gobierno regional"
I_16 = "Iniciativa popular de ley"
I_17 = "Jefatura de gobierno"
I_18 = "Juicio politico, acusacion constitucional"
I_19 = "Justicia constitucional"
I_20 = "Justicia electoral"
I_21 = "Ministerio de educacion"
I_22 = "Ministerio de la familia"
I_23 = "Ministerio de salud"
I_24 = "Ministerio pÃºblico, defensoria publica"
I_25 = "Partidos politicos"
I_26 = "Plebiscitos, referendos y consultas"
I_27 = "Poder judicial, estructura y funciones"
I_28 = "Poderes del estado"
I_29 = "Presidencia de la repÃºblica"
I_30 = "Regimen de gobierno presidencial semi-presidencial parlamentario"
I_31 = "Tribunal constitucional"
I_32 = "Tribunal de defensa de la libre competencia"

TODOS_LOS_CONCEPTOS = [(V_0, V_0), (V_1, V_1), (V_2, V_2), (V_3, V_3), (V_4, V_4), (V_5, V_5), (V_6, V_6), (V_7, V_7), (V_8, V_8), (V_9, V_9), (V_10, V_10), (V_11, V_11), (V_12, V_12), (V_13, V_13), (V_14, V_14), (V_15, V_15), (V_16, V_16), (V_17, V_17), (V_18, V_18), (V_19, V_19), (V_20, V_20), (V_21, V_21), (V_22, V_22), (V_23, V_23), (V_24, V_24), (V_25, V_25), (V_26, V_26), (V_27, V_27), (V_28, V_28), (V_29, V_29), (V_30, V_30), (V_31, V_31), (V_32, V_32), (V_33, V_33), (V_34, V_34), (V_35, V_35), (V_36, V_36), (V_37, V_37), (V_38, V_38), (V_39, V_39), (V_40, V_40), (V_41, V_41), (V_42, V_42), (V_43, V_43), (V_44, V_44), (V_45, V_45), (V_46, V_46), (V_47, V_47), (V_48, V_48), (Der_0, Der_0), (Der_1, Der_1), (Der_2, Der_2), (Der_3, Der_3), (Der_4, Der_4), (Der_5, Der_5), (Der_6, Der_6), (Der_7, Der_7), (Der_8, Der_8), (Der_9, Der_9), (Der_10, Der_10), (Der_11, Der_11), (Der_12, Der_12), (Der_13, Der_13), (Der_14, Der_14), (Der_15, Der_15), (Der_16, Der_16), (Der_17, Der_17), (Der_18, Der_18), (Der_19, Der_19), (Der_20, Der_20), (Der_21, Der_21), (Der_22, Der_22), (Der_23, Der_23), (Der_24, Der_24), (Der_25, Der_25), (Der_26, Der_26), (Der_27, Der_27), (Der_28, Der_28), (Der_29, Der_29), (Der_30, Der_30), (Der_31, Der_31), (Der_32, Der_32), (Der_33, Der_33), (Der_34, Der_34), (Der_35, Der_35), (Der_36, Der_36), (Der_37, Der_37), (Der_38, Der_38), (Der_39, Der_39), (Der_40, Der_40), (Der_41, Der_41), (Der_42, Der_42), (Der_43, Der_43), (Der_44, Der_44), (Der_45, Der_45), (Der_46, Der_46), (Der_47, Der_47), (Der_48, Der_48), (Der_49, Der_49), (Der_50, Der_50), (Der_51, Der_51), (Der_52, Der_52), (Deb_0, Deb_0), (Deb_1, Deb_1), (Deb_2, Deb_2), (Deb_3, Deb_3), (Deb_4, Deb_4), (Deb_5, Deb_5), (Deb_6, Deb_6), (Deb_7, Deb_7), (Deb_8, Deb_8), (Deb_9, Deb_9), (Deb_10, Deb_10), (Deb_11, Deb_11), (Deb_12, Deb_12), (Deb_13, Deb_13), (Deb_14, Deb_14), (Deb_15, Deb_15), (Deb_16, Deb_16), (Deb_17, Deb_17), (I_0, I_0), (I_1, I_1), (I_2, I_2), (I_3, I_3), (I_4, I_4), (I_5, I_5), (I_6, I_6), (I_7, I_7), (I_8, I_8), (I_9, I_9), (I_10, I_10), (I_11, I_11), (I_12, I_12), (I_13, I_13), (I_14, I_14), (I_15, I_15), (I_16, I_16), (I_17, I_17), (I_18, I_18), (I_19, I_19), (I_20, I_20), (I_21, I_21), (I_22, I_22), (I_23, I_23), (I_24, I_24), (I_25, I_25), (I_26, I_26), (I_27, I_27), (I_28, I_28), (I_29, I_29), (I_30, I_30), (I_31, I_31), (I_32, I_32), (I_0, I_0), (I_1, I_1), (I_2, I_2), (I_3, I_3), (I_4, I_4), (I_5, I_5), (I_6, I_6), (I_7, I_7), (I_8, I_8), (I_9, I_9), (I_10, I_10), (I_11, I_11), (I_12, I_12), (I_13, I_13), (I_14, I_14), (I_15, I_15), (I_16, I_16), (I_17, I_17), (I_18, I_18), (I_19, I_19), (I_20, I_20), (I_21, I_21), (I_22, I_22), (I_23, I_23), (I_24, I_24), (I_25, I_25), (I_26, I_26), (I_27, I_27), (I_28, I_28), (I_29, I_29), (I_30, I_30), (I_31, I_31), (I_32, I_32)]


Valores = [
    V_0, V_1, V_2, V_3, V_4, V_5, V_6, V_7, V_8, V_9, V_10, V_11, V_12, V_13, V_14, V_15, V_16, V_17, V_18, V_19, V_20, V_21, V_22, V_23, V_24, V_25, V_26, V_27, V_28, V_29, V_30, V_31, V_32, V_33, V_34, V_35, V_36, V_37, V_38, V_39, V_40, V_41, V_42, V_43, V_44, V_45, V_46, V_47, V_48
]

Derechos = [
    Der_0, Der_1, Der_2, Der_3, Der_4, Der_5, Der_6, Der_7, Der_8, Der_9, Der_10, Der_11, Der_12, Der_13, Der_14, Der_15, Der_16, Der_17, Der_18, Der_19, Der_20, Der_21, Der_22, Der_23, Der_24, Der_25, Der_26, Der_27, Der_28, Der_29, Der_30, Der_31, Der_32, Der_33, Der_34, Der_35, Der_36, Der_37, Der_38, Der_39, Der_40, Der_41, Der_42, Der_43, Der_44, Der_45, Der_46, Der_47, Der_48, Der_49, Der_50, Der_51, Der_52
]

Deberes = [
    Deb_0, Deb_1, Deb_2, Deb_3, Deb_4, Deb_5, Deb_6, Deb_7, Deb_8, Deb_9, Deb_10, Deb_11, Deb_12, Deb_13, Deb_14, Deb_15, Deb_16, Deb_17
]


Instituciones = [
    I_0, I_1, I_2, I_3, I_4, I_5, I_6, I_7, I_8, I_9, I_10, I_11, I_12, I_13, I_14, I_15, I_16, I_17, I_18, I_19, I_20, I_21, I_22, I_23, I_24, I_25, I_26, I_27, I_28, I_29, I_30, I_31, I_32
]


def get_conceptos_Valores():
    return Valores

def get_conceptos_Derechos():
    return Derechos

def get_conceptos_Deberes():
    return Deberes

def get_conceptos_Instituciones():
    return Instituciones

class Post(models.Model):
    title = models.CharField(max_length=100)

    categoria = models.CharField(max_length=200, null=True, choices=CATEGORIAS)
    concepto = models.CharField(max_length=200, choices=TODOS_LOS_CONCEPTOS, null=True)

    content = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200,unique=True)
    #title = models.CharField(max_length=100)
    #content = models.TextField()  # importar el otro field
    #imagen = models.URLField()
    #publish_date = models.DateTimeField(auto_now_add=True)
    #last_update = models.DateTimeField(auto_now = True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #slug = models.SlugField()
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })

    def get_like_url(self):
        return reverse("like", kwargs={
            'slug': self.slug
        })

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

    @property
    def get_dislike_count(self):
        return self.dislike_set.all().count()



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField()

    def __str__(self):
        return self.user


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.user

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

'''
receiver(post_save, sender=Cabildo)
def CrearArticulo(sender, instance, created, **kwargs):
    if created:
        Post.objects.create(user=instance)
        print("cabildo creado yei")
    instance.post.save()
'''