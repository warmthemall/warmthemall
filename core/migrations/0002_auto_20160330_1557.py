# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
