# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0015_story_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
