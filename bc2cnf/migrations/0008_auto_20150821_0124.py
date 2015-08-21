# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0007_auto_20150820_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='userid',
            field=models.CharField(default=b'Y1WO', max_length=8),
        ),
    ]
