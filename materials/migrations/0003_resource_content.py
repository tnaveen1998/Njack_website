# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_auto_20171027_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='content',
            field=models.CharField(default=1, max_length=10000000),
            preserve_default=False,
        ),
    ]
