# Generated by Django 2.2.6 on 2019-10-02 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20191002_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='client',
            name='license_key',
            field=models.CharField(default='OLegRz7NBCOdXIBYcddv', max_length=20, unique=True),
        ),
    ]
