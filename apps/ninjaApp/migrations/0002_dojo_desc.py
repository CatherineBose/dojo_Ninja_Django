# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-16 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]