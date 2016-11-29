# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u7528\u6237\u540d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1\u5730\u5740')),
                ('token', models.CharField(max_length=50, null=True, verbose_name='token\u503c', blank=True)),
                ('verification_status', models.BooleanField(default=False, verbose_name='\u6ce8\u518c\u72b6\u6001')),
                ('authcode', models.CharField(max_length=50, verbose_name='authcode\u503c')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
