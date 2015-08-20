# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0003_auto_20150820_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='datetime',
        ),
    ]
