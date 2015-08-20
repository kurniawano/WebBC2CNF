# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc2cnf', '0004_remove_submission_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='userid',
            field=models.CharField(default=b'WI15', max_length=8),
        ),
        migrations.AlterField(
            model_name='submission',
            name='bcfile',
            field=models.FileField(upload_to=b'files'),
        ),
    ]
