# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 12:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0002_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 12, 26, 12, 770378, tzinfo=utc)),
        ),
    ]