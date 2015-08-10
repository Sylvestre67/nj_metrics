# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_auto_20150810_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='election',
            field=models.ForeignKey(default=1, to='metrics.Election'),
            preserve_default=False,
        ),
    ]
