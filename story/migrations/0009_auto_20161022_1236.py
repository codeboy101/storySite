# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('story', '0008_auto_20161022_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='story',
        ),
        migrations.AddField(
            model_name='vote',
            name='story',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='story.Story'),
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voters',
        ),
        migrations.AddField(
            model_name='vote',
            name='voters',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
