# Generated by Django 2.1.7 on 2019-04-01 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_auto_20190327_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttestmodel',
            name='test_attempt_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
