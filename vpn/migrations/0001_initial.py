# Generated by Django 2.2.1 on 2019-09-24 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VPN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=50)),
                ('ping', models.IntegerField()),
                ('speed', models.CharField(max_length=100)),
                ('numVpnSessions', models.CharField(max_length=50)),
                ('uptime', models.CharField(max_length=50)),
                ('totalUsers', models.CharField(max_length=50)),
                ('totalTraffic', models.CharField(max_length=50)),
                ('log_type', models.CharField(max_length=200)),
                ('operator', models.CharField(max_length=200)),
                ('config_data', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vpns', to='vpn.Country')),
            ],
        ),
    ]