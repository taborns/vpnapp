# Generated by Django 2.2.1 on 2019-09-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0002_auto_20190925_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vpn',
            name='operator',
        ),
    ]
