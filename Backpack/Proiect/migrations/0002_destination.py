# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proiect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination_name', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
            ],
        ),
    ]
