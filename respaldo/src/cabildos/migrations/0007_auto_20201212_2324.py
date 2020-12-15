# Generated by Django 3.1.3 on 2020-12-13 02:24

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cabildos', '0006_merge_20201212_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabildo',
            name='categoria',
            field=models.CharField(choices=[('Valores', 'Valores'), ('Derechos', 'Derechos'), ('Deberes', 'Deberes'), ('Instituciones', 'Instituciones')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cabildo',
            name='etiquetas',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Valores Derechos', 'Valores Derechos'), ('Amistad civica', 'Amistad civica'), ('Autonomia libertad', 'Autonomia libertad'), ('Bien comun comunidad', 'Bien comun comunidad'), ('Buen vivir', 'Buen vivir'), ('Ciudadania', 'Ciudadania'), ('Democracia', 'Democracia'), ('Desarrollo', 'Desarrollo'), ('Desarrollo sustentable', 'Desarrollo sustentable'), ('Descentralizacion', 'Descentralizacion'), ('Dignidad', 'Dignidad'), ('Diversidad', 'Diversidad'), ('Emprendimiento libre', 'Emprendimiento libre'), ('Equidad de gÃ©nero', 'Equidad de gÃ©nero'), ('Estado de derecho', 'Estado de derecho'), ('Estado garante', 'Estado garante'), ('Estado laico', 'Estado laico'), ('Estado solidario', 'Estado solidario'), ('Familia', 'Familia'), ('Felicidad', 'Felicidad'), ('Fraternidad', 'Fraternidad'), ('Identidad cultural', 'Identidad cultural'), ('Igualdad', 'Igualdad'), ('Igualdad de oportunidades', 'Igualdad de oportunidades'), ('Inclusion', 'Inclusion'), ('Innovacion creatividad', 'Innovacion creatividad'), ('Integracion', 'Integracion'), ('Justicia', 'Justicia'), ('Justicia social', 'Justicia social'), ('Medio ambiente', 'Medio ambiente'), ('Multiculturalidad', 'Multiculturalidad'), ('Participacion ciudadana', 'Participacion ciudadana'), ('Patriotismo', 'Patriotismo'), ('Paz convivencia pacifica', 'Paz convivencia pacifica'), ('Pluralismo', 'Pluralismo'), ('Plurinacionalismo', 'Plurinacionalismo'), ('Probidad', 'Probidad'), ('Republica', 'Republica'), ('Respeto', 'Respeto'), ('Respeto conservacion de la naturaleza o medio ambiente', 'Respeto conservacion de la naturaleza o medio ambiente'), ('Seguridad', 'Seguridad'), ('Soberania', 'Soberania'), ('Soberania popular', 'Soberania popular'), ('Solidaridad', 'Solidaridad'), ('Subsidiaridad', 'Subsidiaridad'), ('Tolerancia', 'Tolerancia'), ('Transparencia', 'Transparencia'), ('Transparencia y publicidad', 'Transparencia y publicidad'), ('Unidad', 'Unidad')], max_length=300),
        ),
        migrations.AlterField(
            model_name='cabildo',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='cabildo',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
