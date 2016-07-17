# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testobfuscator', '0002_mymodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=b'Date', blank=True),
        ),
    ]
