# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0006_auto_20150820_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='userid',
            field=models.CharField(default=b'73FO', max_length=8),
        ),
    ]
