# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 14:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('society_members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='age',
        ),
        migrations.RemoveField(
            model_name='members',
            name='mobile_number',
        ),
    ]
