# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-09-30 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_remove_tipobono_prevision'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipobono',
            name='prevision',
            field=models.ManyToManyField(through='registro.BonoPrevision', to='registro.Prevision'),
        ),
    ]
