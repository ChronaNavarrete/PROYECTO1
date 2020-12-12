from quickchart import QuickChart
from static import archivos

def crearpost(id_cabildo):
    #if not realizado:
    pass

def creargrafico():
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.device_pixel_ratio = 2.0
    qc.config = { 
        "type": "bar",
        "data": {
            "labels": ["Hello world", "Test"],
            "datasets": [{
                "label": "Foo",
                "data": [1, 2]
            }]
        }
    }
    return qc.get_url()


lista_categorias = ['Valores','Derechos','Deberes','Instituciones']

lista_Valores = ['Valores Derechos', 'Amistad civica', 'Autonomia libertad', 'Bien comun comunidad', 'Buen vivir', 'Ciudadania', 'Democracia', 'Desarrollo', 'Desarrollo sustentable', 'Descentralizacion', 'Dignidad', 'Diversidad', 'Emprendimiento libre', 'Equidad de gÃ©nero', 'Estado de derecho', 'Estado garante', 'Estado laico', 'Estado solidario', 'Familia', 'Felicidad', 'Fraternidad', 'Identidad cultural', 'Igualdad', 'Igualdad de oportunidades', 'Inclusion', 'Innovacion creatividad', 'Integracion', 'Justicia', 'Justicia social', 'Medio ambiente', 'Multiculturalidad', 'ParticipaciÃ³n ciudadana', 'Patriotismo', 'Paz convivencia pacifica', 'Pluralismo', 'Plurinacionalismo', 'Probidad', 'Republica', 'Respeto', 'Respeto conservacion de la naturaleza o medio ambiente', 'Seguridad', 'Soberania', 'Soberania popular', 'Solidaridad', 'Subsidiaridad', 'Tolerancia', 'Transparencia', 'Transparencia y publicidad', 'Unidad']
lista_Derechos = ['A huelga', 'A la educacion', 'A la honra, al honor', 'A la identidad cultural', 'A la informacion', 'A la integracion de discapacidad', 'A la integridad fisica y psiquica', 'A la nacionalidad', 'A la participacion', 'A la salud', 'A la seguridad social', 'A la seguridad vida sin violencia', 
'A la vida', 'A la vida digna', 'A la vivienda digna', 'A sindicalizarse y a la negociacion colectiva', 'A sufragio votar', 'Acceso a informacion publica', 'Acceso a la cultura', 'Al agua', 'Al salario equitativo', 'Al trabajo', 'Articulo 19', 'De los pueblos indigenas', 'De peticion ante las autoridades', 'De propiedad', 'Derecho al agua', 'Derecho de asociacion', 'Derechos del niÃ±o, niÃ±a y adolescente', 'Igualdad ante la ley', 'Igualdad ante las cargas publicas', 'Igualdad ante los tributos', 'Igualdad de acceso a la justicia debido proceso', 'Igualdad de genero', 'Jubilacion digna', 'Libertad ambulatoria', 'Libertad de conciencia', 'Libertad de culto', 'Libertad de enseñanza', 'Libertad de expresion', 'Libertad de trabajo', 'Libertad personal', 'Libertad religiosa', 'Libre iniciativa economica, libre empresa', 'No discriminacion', 'Privacidad e intimidad', 'Proteccion judicial de los derechos', 'Respeto a la naturaleza medio ambiente', 'Reunion pacifica', 'Seguridad social', 'Ser elegido en cargos publicos', 'Sexuales y reproductivos', 'Trabajo digno']
lista_Deberes = ['Cumplimiento de las leyes y normas', 'Cumplimiento de obligaciones fiscales', 'Cumplimiento de tratados y obligaciones internacionales', 'De proteccion y conservacion de patrimonio historico y cultural', 'De satisfacer cargas publicas', 'Deber de transparencia en los actos de gobierno', 'Deberes de proteccion de conservacion de la naturaleza', 'Educacion civica', 'Ejercicio legitimo y no abusivo de los derechos', 'Promocion de los derechos fundamentales', 'Proteccion, promocion y respeto de los derechos humanos y fundamentales', 'Respeto de derechos de otros', 'Respeto por la constitucion', 'Responsabilidad', 'Responsabilidad civica', 'Servicio a la comunidad', 'Unidad nacional y respeto por chile', 'Voto obligatorio']
lista_Instituciones = ['Asamblea constituyente', 'Banco central', 'Cambio o reforma constitucional', 'Congreso o parlamento, estructura y funciones', 'Congreso unicameral', 'Contraloria general tribunales de cuentas', 'Defensor del pueblo ciudadano', 'Division territorial', 'Estado de excepcion', 'Fiscalizacion', 'Forma de estado, federalismo autonomias regionales', 'Fuerzas armadas', 'Gobierno local municipal', 'Gobierno nacional estructura y funciones', 'Gobierno provincial', 'Gobierno regional', 'Iniciativa popular de ley', 'Jefatura de gobierno', 'Juicio politico, acusacion constitucional', 'Justicia constitucional', 'Justicia electoral', 'Ministerio de educacion', 'Ministerio de la familia', 'Ministerio de salud', 'Ministerio pÃºblico, defensoria publica', 'Partidos politicos', 'Plebiscitos, referendos y consultas', 'Poder judicial, estructura y funciones', 'Poderes del estado', 'Presidencia de la repÃºblica', 'Regimen de gobierno presidencial semi-presidencial parlamentario', 'Tribunal constitucional', 'Tribunal de defensa de la libre competencia']

img = creargrafico()
print(img)
