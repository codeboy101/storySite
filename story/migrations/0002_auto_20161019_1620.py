# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='header',
            new_name='title',
        ),
    ]
