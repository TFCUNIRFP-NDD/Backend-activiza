# Generated by Django 5.0.4 on 2024-04-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activiza', '0008_usuario_alumnos_usuario_objetivo_publicaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='alumnos',
            field=models.ManyToManyField(blank=True, to='activiza.usuario'),
        ),
    ]
