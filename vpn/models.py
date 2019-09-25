from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=50)

class VPN(models.Model):
    hostname = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    score = models.CharField(max_length=50)
    ping = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name = 'vpns')
    numVpnSessions = models.CharField(max_length=50)
    uptime = models.CharField(max_length=50)
    totalUsers = models.CharField(max_length=50)
    totalTraffic = models.CharField(max_length=50)
    log_type = models.CharField(max_length=200)
    config_data = models.TextField()

    class Meta:
        ordering = '-score',



