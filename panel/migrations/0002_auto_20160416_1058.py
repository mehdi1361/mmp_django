# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='service',
            name='name_persian',
            field=models.CharField(help_text='service persian name', max_length=40, verbose_name='service_name_persian'),
        ),
        migrations.AlterModelTable(
            name='service',
            table='services',
        ),
    ]
