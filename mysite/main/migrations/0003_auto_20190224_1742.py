# Generated by Django 2.1.7 on 2019-02-24 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190224_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='replace-me'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 24, 17, 41, 7, 308837), verbose_name='date published'),
        ),
    ]