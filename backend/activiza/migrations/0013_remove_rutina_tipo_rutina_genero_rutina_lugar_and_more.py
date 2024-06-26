# Generated by Django 5.0.4 on 2024-05-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activiza', '0012_alter_entrenador_options_alter_publicacion_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rutina',
            name='tipo',
        ),
        migrations.AddField(
            model_name='rutina',
            name='genero',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], default='H', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rutina',
            name='lugar',
            field=models.CharField(choices=[('C', 'Casa'), ('G', 'Gimnasio')], default='C', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rutina',
            name='objetivo',
            field=models.CharField(choices=[('PG', 'Perder grasa'), ('GM', 'Ganar musculo')], default='PG', max_length=2),
            preserve_default=False,
        ),
    ]
