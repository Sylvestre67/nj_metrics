# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField(null=True)),
                ('county', models.ForeignKey(to='metrics.County')),
            ],
        ),
        migrations.DeleteModel(
            name='Year',
        ),
        migrations.AddField(
            model_name='party',
            name='code',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='number',
            field=models.BigIntegerField(default=0),
        ),
    ]
