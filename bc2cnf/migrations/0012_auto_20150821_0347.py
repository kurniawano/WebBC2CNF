# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0011_auto_20150821_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='bcfile',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='submission',
            name='userid',
            field=models.CharField(default=b'GHQW', max_length=8),
        ),
    ]
