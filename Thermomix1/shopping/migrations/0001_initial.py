# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('creation_date', models.DateField(verbose_name='Fecha de creaci\xf3n')),
                ('made_date', models.DateField(verbose_name='Fecha de compra')),
                ('made', models.BooleanField(default=False, verbose_name='Compra realizada')),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredients')),
            ],
            options={
                'verbose_name': 'Lista de la compra',
                'verbose_name_plural': 'Listas de la compra',
            },
            bases=(models.Model,),
        ),
    ]
