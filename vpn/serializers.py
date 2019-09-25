from rest_framework import serializers
from vpn import models 
from django.utils.http import urlsafe_base64_decode 

class VPNSerializer(serializers.ModelSerializer):

    config_data = serializers.SerializerMethodField()
    
    def get_config_data(self, obj):
        return urlsafe_base64_decode(obj.config_data)

    class Meta:
        model = models.VPN
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country 
        fields = '__all__'

class VPNCountrySerializer(VPNSerializer):

    country = CountrySerializer(read_only=True)

class CountryVPNSerializer(CountrySerializer):

    vpns = VPNSerializer(read_only=True,many=True)

    