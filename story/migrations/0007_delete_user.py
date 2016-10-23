# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_auto_20161020_1218'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
