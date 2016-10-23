# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('header', models.CharField(max_length=75)),
                ('body', models.TextField()),
                ('total', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
