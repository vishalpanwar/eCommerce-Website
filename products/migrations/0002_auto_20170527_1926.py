# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 19:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-name']},
        ),
    ]
