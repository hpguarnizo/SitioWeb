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
            name='Foro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(auto_now=True)),
                ('contenido', models.TextField(max_length=10000)),
                ('apropiado', models.BooleanField(default=1)),
                ('esRespuesta', models.BooleanField(default=0)),
                ('autor', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL)),
                ('respuestaDe', models.ForeignKey(related_name='respuesta', null=True, to='Foro.Mensaje')),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, verbose_name='Foto de perfil', null=True, upload_to='/media/')),
                ('mensajes', models.IntegerField(default=0)),
                ('actualizacion', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('foro', models.ForeignKey(related_name='temas', to='Foro.Foro')),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.AddField(
            model_name='mensaje',
            name='tema',
            field=models.ForeignKey(related_name='mensajes', to='Foro.Tema'),
        ),
    ]
