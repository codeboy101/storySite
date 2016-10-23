# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_auto_20161020_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='has_voted',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=25),
            preserve_default=True,
        ),
    ]
