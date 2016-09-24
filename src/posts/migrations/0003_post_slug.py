# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-18 12:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 9, 18, 12, 56, 22, 762891, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
