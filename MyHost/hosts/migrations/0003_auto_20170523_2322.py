# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_auto_20170523_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='function',
            new_name='name',
        ),
    ]