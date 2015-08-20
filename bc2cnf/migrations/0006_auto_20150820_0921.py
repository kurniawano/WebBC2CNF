# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0005_auto_20150820_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='userid',
            field=models.CharField(default=b'PO1F', max_length=8),
        ),
    ]
