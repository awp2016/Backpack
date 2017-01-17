# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=100)),
                ('Date_added', models.DateTimeField(auto_now_add=True)),
                ('Avatar', models.ImageField(null=True, upload_to='images')),
                ('Rating', models.IntegerField()),
=======
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination_name', models.CharField(max_length=200)),
                ('Country', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
>>>>>>> ea9c25f6bb484603a78e6adeab7df6699148ed0c
            ],
        ),
    ]
