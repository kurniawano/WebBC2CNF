# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
