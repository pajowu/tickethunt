# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_tickettype_show_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickettype',
            name='comment',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]