# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('idc', models.CharField(blank=True, max_length=20, null=True)),
                ('port', models.IntegerField(default='22')),
                ('os', models.CharField(default='linux', max_length=20, verbose_name='Operating System')),
                ('user', models.CharField(default='root', max_length=20, verbose_name='manage user')),
                ('passwd', models.CharField(max_length=20, verbose_name='manage passwd')),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
    ]
