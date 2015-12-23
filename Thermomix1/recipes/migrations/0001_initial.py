# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import recipes.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.CharField(max_length=800, verbose_name='Descripci\xf3n')),
            ],
            options={
                'verbose_name': 'Materia prima',
                'verbose_name_plural': 'Materias primas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='C\xf3digo')),
                ('name', models.CharField(max_length=300, verbose_name='Nombre')),
                ('valid', models.BooleanField(default=True, verbose_name='V\xe1lido')),
            ],
            options={
                'verbose_name': 'Categor\xeda',
                'verbose_name_plural': 'Categor\xedas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(null=True, verbose_name='Cantidad', blank=True)),
                ('detalle', models.CharField(max_length=500, null=True, verbose_name='Detalle', blank=True)),
                ('bom', models.ForeignKey(verbose_name='Materias primas', to='recipes.Bom')),
            ],
            options={
                'verbose_name': 'Ingrediente',
                'verbose_name_plural': 'Ingredientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='T\xedtulo')),
                ('description', models.TextField(null=True, verbose_name='Descripci\xf3n', blank=True)),
                ('autor', models.CharField(max_length=200, null=True, verbose_name='Autor', blank=True)),
                ('is_thermomix', models.BooleanField(default=True, verbose_name='Thermomix')),
                ('create_date', models.DateTimeField(verbose_name='Fecha de creaci\xf3n')),
                ('version', models.CharField(default=b'1.0', max_length=100, verbose_name='Versi\xf3n')),
                ('preparation', models.TextField(verbose_name='Preparaci\xf3n')),
                ('aclaraciones', models.TextField(null=True, verbose_name='Aclaraciones', blank=True)),
                ('sugerencias', models.TextField(null=True, verbose_name='Sugerencias', blank=True)),
                ('saveBy', models.ForeignKey(verbose_name='Usuario', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('creation_date', models.DateTimeField()),
                ('recipe', models.ForeignKey(verbose_name='Receta', to='recipes.Recipe')),
                ('user', models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_image', sorl.thumbnail.fields.ImageField(upload_to=recipes.models.content_file_name)),
                ('recipe', models.ForeignKey(verbose_name='Receta', to='recipes.Recipe')),
                ('user', models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Im\xe1genes de receta',
                'verbose_name_plural': 'Im\xe1genes de recetas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('code', models.CharField(max_length=10, serialize=False, verbose_name='C\xf3digo', primary_key=True)),
                ('description', models.CharField(max_length=100, verbose_name='Descripci\xf3n')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFavoriteRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorite', models.BooleanField(default=False, verbose_name='Favorita')),
                ('times', models.IntegerField(verbose_name='Veces usada')),
                ('recipe', models.ForeignKey(verbose_name='Receta', to='recipes.Recipe')),
                ('user', models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Recetas de usuario',
                'verbose_name_plural': 'Recetas de usuario',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(verbose_name='Receta', to='recipes.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredients',
            name='units',
            field=models.ForeignKey(verbose_name='Unidades', blank=True, to='recipes.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bom',
            name='category',
            field=models.ForeignKey(verbose_name='Categor\xeda', to='recipes.Category'),
            preserve_default=True,
        ),
    ]
