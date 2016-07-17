# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testobfuscator', '0003_auto_20160717_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='date',
            field=models.DateField(null=True, verbose_name=b'Date', blank=True),
        ),
    ]
