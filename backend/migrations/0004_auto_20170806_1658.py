# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20170806_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='author',
            new_name='teacher',
        ),
    ]