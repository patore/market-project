# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20160228_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
