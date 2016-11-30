# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(unique=True, max_length=254, verbose_name='\u90ae\u7bb1\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(unique=True, max_length=10, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
