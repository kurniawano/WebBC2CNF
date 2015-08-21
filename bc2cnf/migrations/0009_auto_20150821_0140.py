# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0008_auto_20150821_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='userid',
            field=models.CharField(default=b'TB38', max_length=8),
        ),
    ]
