# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20161019_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='total',
            new_name='rating',
        ),
    ]
