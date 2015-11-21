# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField(help_text=b'Realiza un comentario', verbose_name=b'Comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(unique=True, max_length=10, verbose_name=b'Cedula')),
                ('nombres', models.TextField(help_text=b'Escribe tus nombres', max_length=30)),
                ('apellidos', models.TextField(help_text=b'Escribe tus apellidos', max_length=30)),
                ('celular', models.CharField(unique=True, max_length=10, verbose_name=b'Celular')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='paciente',
            field=models.ForeignKey(to='proyectoFinal.Paciente'),
        ),
    ]
