# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20161020_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='has_voted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='story',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=25),
            preserve_default=True,
        ),
    ]
