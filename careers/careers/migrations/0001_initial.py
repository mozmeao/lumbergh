# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_id', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('apply_url', models.URLField()),
                ('source', models.CharField(max_length=100)),
            ],
        ),
    ]
