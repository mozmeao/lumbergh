# Generated by Django 2.2.24 on 2021-07-28 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210728_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeindexpage',
            name='heroHeader',
        ),
        migrations.RemoveField(
            model_name='homeindexpage',
            name='heroText',
        ),
        migrations.AddField(
            model_name='homeindexpage',
            name='heroOneHeader',
            field=models.CharField(default='temp', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeindexpage',
            name='heroOneText',
            field=models.CharField(default='temp', max_length=255),
            preserve_default=False,
        ),
    ]