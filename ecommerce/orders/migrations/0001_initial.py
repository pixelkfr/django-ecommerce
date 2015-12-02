# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('marketplace', models.CharField(max_length=100)),
                ('order_purchase_date', models.DateField(verbose_name=b'purchase date')),
                ('order_amount', models.FloatField()),
                ('order_id', models.CharField(max_length=19, serialize=False, primary_key=True)),
            ],
        ),
    ]
