# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-01 23:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro')),
                ('project', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('selling', models.BooleanField(choices=[(True, 'à venda'), (False, 'vendido')], default=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('building_type', models.CharField(blank=True, max_length=200)),
                ('unity', models.PositiveIntegerField(default=0)),
                ('face', models.CharField(choices=[('N', 'Norte'), ('S', 'Sul'), ('L', 'Leste'), ('O', 'Oest')], default='S', max_length=1)),
                ('empty', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True)),
                ('selling_price', models.PositiveIntegerField(default=0)),
                ('iptu', models.PositiveIntegerField(default=0)),
                ('square_meters', models.PositiveIntegerField(default=0)),
                ('units_per_floor', models.PositiveIntegerField(blank=True, default=0)),
                ('janitor_name', models.CharField(blank=True, max_length=200)),
                ('parking_slots', models.PositiveIntegerField(default=0)),
                ('bedrooms', models.PositiveIntegerField(default=0)),
                ('washrooms', models.PositiveIntegerField(default=0)),
                ('suites', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.Build')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, default='+55', max_length=6, validators=[django.core.validators.RegexValidator(message='Um código de país pode ou não começar com um sinal demais(+) e deve conter até 6 valores. Um valor pode ser umdígito(0-9), um ponto(.) ou um hífen(-).', regex='^\\+[\\d\\-\\.]{1,6}$')])),
                ('state', models.CharField(default='011', max_length=3, validators=[django.core.validators.RegexValidator(message='Um código de região deve conter até 3 dígitos(0-9).', regex='\\d{2,3}$')])),
                ('number', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Um número de telefone deve conter de 8 a 9 dígitos(0-9).', regex='\\d{8,9}$')])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('picture_file', models.ImageField(blank=True, null=True, upload_to='imoveis.PictureFile/bytes/filename/mimetype')),
            ],
        ),
        migrations.CreateModel(
            name='PictureFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='build',
            name='features',
            field=models.ManyToManyField(blank=True, to='imoveis.Feature'),
        ),
        migrations.AddField(
            model_name='build',
            name='owners',
            field=models.ManyToManyField(blank=True, to='imoveis.Owner'),
        ),
        migrations.AddField(
            model_name='build',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='imoveis.Picture'),
        ),
    ]
