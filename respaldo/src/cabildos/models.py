from django.db import models
from django.forms import ModelForm
from datetime import datetime, date
from multiselectfield import MultiSelectField


# Create your models here.

'''class Categorias(models.Model):
    CATEGORIAS = (
        ('Valores', 'Valores'),
        ('Derechos', 'Derechos'),
        ('Deberes', 'Deberes'),
        ('Instituciones', 'Instituciones'),
    )

    cat = models.CharField(max_length=200, null=False, choices=CATEGORIAS)
    
    def __str__(self):
        return self.cat

class Conceptos(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.categoria



Valores = [
        ('Valores Derechos', 'Valores Derechos'), ('Amistad civica', 'Amistad civica'), ('Autonomia libertad', 'Autonomia libertad'), ('Bien comun comunidad', 'Bien comun comunidad'), ('Buen vivir', 'Buen vivir'), ('Ciudadania', 'Ciudadania'), ('Democracia', 'Democracia'), ('Desarrollo', 'Desarrollo'), ('Desarrollo sustentable', 'Desarrollo sustentable'), ('Descentralizacion', 'Descentralizacion'), ('Dignidad', 'Dignidad'), ('Diversidad', 'Diversidad'), ('Emprendimiento libre', 'Emprendimiento libre'), ('Equidad de gÃ©nero', 'Equidad de gÃ©nero'), ('Estado de derecho', 'Estado de derecho'), ('Estado garante', 'Estado garante'), ('Estado laico', 'Estado laico'), ('Estado solidario', 'Estado solidario'), ('Familia', 'Familia'), ('Felicidad', 'Felicidad'), ('Fraternidad', 'Fraternidad'), ('Identidad cultural', 'Identidad cultural'), ('Igualdad', 'Igualdad'), ('Igualdad de oportunidades', 'Igualdad de oportunidades'), ('Inclusion', 'Inclusion'), ('Innovacion creatividad', 'Innovacion creatividad'), ('Integracion', 'Integracion'), ('Justicia', 'Justicia'), ('Justicia social', 'Justicia social'), ('Medio ambiente', 'Medio ambiente'), ('Multiculturalidad', 'Multiculturalidad'), ('Participacion ciudadana', 'Participacion ciudadana'), ('Patriotismo', 'Patriotismo'), ('Paz convivencia pacifica', 'Paz convivencia pacifica'), ('Pluralismo', 'Pluralismo'), ('Plurinacionalismo', 'Plurinacionalismo'), ('Probidad', 'Probidad'), ('Republica', 'Republica'), ('Respeto', 'Respeto'), ('Respeto conservacion de la naturaleza o medio ambiente', 'Respeto conservacion de la naturaleza o medio ambiente'), ('Seguridad', 'Seguridad'), ('Soberania', 'Soberania'), ('Soberania popular', 'Soberania popular'), ('Solidaridad', 'Solidaridad'), ('Subsidiaridad', 'Subsidiaridad'), ('Tolerancia', 'Tolerancia'), ('Transparencia', 'Transparencia'), ('Transparencia y publicidad', 'Transparencia y publicidad'), ('Unidad', 'Unidad')
]
Derechos = [
        ('A huelga', 'A huelga'), ('A la educacion', 'A la educacion'), ('A la honra, al honor', 'A la honra, al honor'), ('A la identidad cultural', 'A la identidad cultural'), ('A la informacion', 'A la informacion'), ('A la integracion de discapacidad', 'A la integracion de discapacidad'), ('A la integridad fisica y psiquica', 'A la integridad fisica y psiquica'), ('A la nacionalidad', 'A la nacionalidad'), ('A la participacion', 'A la participacion'), ('A la salud', 'A la salud'), ('A la seguridad social', 'A la seguridad social'), ('A la seguridad vida sin violencia', 'A la seguridad vida sin violencia'), ('A la vida', 'A la vida'), ('A la vida digna', 'A la vida digna'), ('A la vivienda digna', 'A la vivienda digna'), ('A sindicalizarse y a la negociacion colectiva', 'A sindicalizarse y a la negociacion colectiva'), ('A sufragio votar', 'A sufragio votar'), ('Acceso a informacion publica', 'Acceso a informacion publica'), ('Acceso a la cultura', 'Acceso a la cultura'), ('Al agua', 'Al agua'), ('Al salario equitativo', 'Al salario equitativo'), ('Al trabajo', 'Al trabajo'), ('Articulo 19', 'Articulo 19'), ('De los pueblos indigenas', 'De los pueblos indigenas'), ('De peticion ante las autoridades', 'De peticion ante las autoridades'), ('De propiedad', 'De propiedad'), ('Derecho al agua', 'Derecho al agua'), ('Derecho de asociacion', 'Derecho de asociacion'), ('Derechos del niño, niña y adolescente', 'Derechos del niño, niña y adolescente'), ('Igualdad ante la ley', 'Igualdad ante la ley'), ('Igualdad ante las cargas publicas', 'Igualdad ante las cargas publicas'), ('Igualdad ante los tributos', 'Igualdad ante los tributos'), ('Igualdad de acceso a la justicia debido proceso', 'Igualdad de acceso a la justicia debido proceso'), ('Igualdad de genero', 'Igualdad de genero'), ('Jubilacion digna', 'Jubilacion digna'), ('Libertad ambulatoria', 'Libertad ambulatoria'), ('Libertad de conciencia', 'Libertad de conciencia'), ('Libertad de culto', 'Libertad de culto'), ('Libertad de enseñanza', 'Libertad de enseñanza'), ('Libertad de expresion', 'Libertad de expresion'), ('Libertad de trabajo', 'Libertad de trabajo'), ('Libertad personal', 'Libertad personal'), ('Libertad religiosa', 'Libertad religiosa'), ('Libre iniciativa economica, libre empresa', 'Libre iniciativa economica, libre empresa'), ('No discriminacion', 'No discriminacion'), ('Privacidad e intimidad', 'Privacidad e intimidad'), ('Proteccion judicial de los derechos', 'Proteccion judicial de los derechos'), ('Respeto a la naturaleza medio ambiente', 'Respeto a la naturaleza medio ambiente'), ('Reunion pacifica', 'Reunion pacifica'), ('Seguridad social', 'Seguridad social'), ('Ser elegido en cargos publicos', 'Ser elegido en cargos publicos'), ('Sexuales y reproductivos', 'Sexuales y reproductivos'), ('Trabajo digno', 'Trabajo digno')
]
Deberes = [
    ('Cumplimiento de las leyes y normas', 'Cumplimiento de las leyes y normas'), ('Cumplimiento de obligaciones fiscales', 'Cumplimiento de obligaciones fiscales'), ('Cumplimiento de tratados y obligaciones internacionales', 'Cumplimiento de tratados y obligaciones internacionales'), ('De proteccion y conservacion de patrimonio historico y cultural', 'De proteccion y conservacion de patrimonio historico y cultural'), ('De satisfacer cargas publicas', 'De satisfacer cargas publicas'), ('Deber de transparencia en los actos de gobierno', 'Deber de transparencia en los actos de gobierno'), ('Deberes de proteccion de conservacion de la naturaleza', 'Deberes de proteccion de conservacion de la naturaleza'), ('Educacion civica', 'Educacion civica'), ('Ejercicio legitimo y no abusivo de los derechos', 'Ejercicio legitimo y no abusivo de los derechos'), ('Promocion de los derechos fundamentales', 'Promocion de los derechos fundamentales'), ('Proteccion, promocion y respeto de los derechos humanos y fundamentales', 'Proteccion, promocion y respeto de los derechos humanos y fundamentales'), ('Respeto de derechos de otros', 'Respeto de derechos de otros'), ('Respeto por la constitucion', 'Respeto por la constitucion'), ('Responsabilidad', 'Responsabilidad'), ('Responsabilidad civica', 'Responsabilidad civica'), ('Servicio a la comunidad', 'Servicio a la comunidad'), ('Unidad nacional y respeto por chile', 'Unidad nacional y respeto por chile'), ('Voto obligatorio', 'Voto obligatorio')
]
Instituciones = [
    ('Asamblea constituyente', 'Asamblea constituyente'), ('Banco central', 'Banco central'), ('Cambio o reforma constitucional', 'Cambio o reforma constitucional'), ('Congreso o parlamento, estructura y funciones', 'Congreso o parlamento, estructura y funciones'), ('Congreso unicameral', 'Congreso unicameral'), ('Contraloria general tribunales de cuentas', 'Contraloria general tribunales de cuentas'), ('Defensor del pueblo ciudadano', 'Defensor del pueblo ciudadano'), ('Division territorial', 'Division territorial'), ('Estado de excepcion', 'Estado de excepcion'), ('Fiscalizacion', 'Fiscalizacion'), ('Forma de estado, federalismo autonomias regionales', 'Forma de estado, federalismo autonomias regionales'), ('Fuerzas armadas', 'Fuerzas armadas'), ('Gobierno local municipal', 'Gobierno local municipal'), ('Gobierno nacional estructura y funciones', 'Gobierno nacional estructura y funciones'), ('Gobierno provincial', 'Gobierno provincial'), ('Gobierno regional', 'Gobierno regional'), ('Iniciativa popular de ley', 'Iniciativa popular de ley'), ('Jefatura de gobierno', 'Jefatura de gobierno'), ('Juicio politico, acusacion constitucional', 'Juicio politico, acusacion constitucional'), ('Justicia constitucional', 'Justicia constitucional'), ('Justicia electoral', 'Justicia electoral'), ('Ministerio de educacion', 'Ministerio de educacion'), ('Ministerio de la familia', 'Ministerio de la familia'), ('Ministerio de salud', 'Ministerio de salud'), ('Ministerio pÃºblico, defensoria publica', 'Ministerio pÃºblico, defensoria publica'), ('Partidos politicos', 'Partidos politicos'), ('Plebiscitos, referendos y consultas', 'Plebiscitos, referendos y consultas'), ('Poder judicial, estructura y funciones', 'Poder judicial, estructura y funciones'), ('Poderes del estado', 'Poderes del estado'), ('Presidencia de la repÃºblica', 'Presidencia de la repÃºblica'), ('Regimen de gobierno presidencial semi-presidencial parlamentario', 'Regimen de gobierno presidencial semi-presidencial parlamentario'), ('Tribunal constitucional', 'Tribunal constitucional'), ('Tribunal de defensa de la libre competencia', 'Tribunal de defensa de la libre competencia')
]

'''

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





class Cabildo(models.Model):
    categoria = models.CharField(max_length=200, null=True, choices=CATEGORIAS)
    concepto = models.CharField(max_length=200, choices=TODOS_LOS_CONCEPTOS)
    nombre = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now_add=False)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre



'''sql 
    id
    etiquetas = conceptos = temas constitucionales # filtar el archivo bachele 2016
    nombre
    fecha
    hora
    #link
    realizado True False
    conclusion = str
    aprobacion = %


lista_categorias = ['Valores','Derechos','Deberes','Instituciones']
'''