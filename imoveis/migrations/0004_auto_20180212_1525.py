# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-12 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_auto_20180204_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='build',
            name='district',
        ),
        migrations.AddField(
            model_name='build',
            name='district',
            field=models.ManyToManyField(blank=True, to='imoveis.District', verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='build',
            name='owners',
            field=models.ManyToManyField(blank=True, to='imoveis.Owner', verbose_name='Proprietários'),
        ),
    ]
