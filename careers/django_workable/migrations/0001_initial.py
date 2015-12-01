# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shortcode', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=150, null=True, blank=True)),
                ('detail_url', models.URLField()),
                ('apply_url', models.URLField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(blank=True, to='django_workable.Category', null=True)),
            ],
        ),
    ]
