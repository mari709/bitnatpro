# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-14 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitnat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='estado',
        ),
    ]
