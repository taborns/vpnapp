from django.shortcuts import render
from vpn import serializers, models, scrapper
from rest_framework import generics,views
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.
class VPNListView( generics.ListAPIView ):

    serializer_class = serializers.VPNSerializer
    queryset = models.VPN.objects.all()


    def list(self, request, countryID):

        country = models.Country.objects.get(pk=countryID)
        vpns = country.vpns.all()
        vpns = self.paginate_queryset(vpns)
        serializer_class = self.get_serializer( vpns , many=True )

        return Response(serializer_class.data )

class CountryView( generics.ListAPIView ):

    serializer_class = serializers.CountrySerializer 
    queryset = models.Country.objects.all() 
    

class RandomVPNView( generics.ListAPIView):
    
    serializer_class = serializers.VPNCountrySerializer 
    queryset = models.VPN.objects.all() 
        
    def list(self, request):
        
        vpns = models.VPN.objects.all()[:10]
        serializer = self.get_serializer(vpns, many=True)
        return Response(serializer.data)


class VPNScrapper( views.APIView):

    serializer_class = serializers.VPNSerializer
    queryset = models.VPN.objects.all() 

    def  get(self, request, format=None):
        scrapper.scrapVPNS('/Users/mac/Desktop/vpndata.csv')
        return Response('SCRAP DONE')
