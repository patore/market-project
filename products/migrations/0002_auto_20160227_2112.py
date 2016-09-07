# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=b'description here'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default=b'title here', max_length=100),
        ),
    ]
