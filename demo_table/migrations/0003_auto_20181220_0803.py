# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-20 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_table', '0002_auto_20181220_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=200, null=True, verbose_name='评论量'),
        ),
    ]
