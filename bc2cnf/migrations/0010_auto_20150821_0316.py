# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0009_auto_20150821_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='userid',
            field=models.CharField(default=b'FW24', max_length=8),
        ),
    ]
