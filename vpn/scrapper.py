import csv 
from vpn import models 
import requests
from io import StringIO
def scrapVPNS(url):
    print("URL", url)
    headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    response = requests.get(url)

    csv_reader = csv.reader(StringIO(response.text), delimiter=',')
    #csv_reader = csv.reader(ftpstream.read().decode('utf-8'))  # with the appropriate encoding 

    line_count = 0
    
    vpn_pks = []

    for row in csv_reader:
        line_count += 1

        if line_count < 3 or len(row) != 15:
            continue
        else:
            hostname, ip, score, ping, speed, country, country_short, numVpnSessions, uptime, total_users, total_traffic, log_type, operator, message, config_data = row 
            try:
                country = models.Country.objects.get(short=country_short)
            except:
                country = models.Country.objects.create(name=country, short=country_short)
            vpn = models.VPN.objects.create(

                hostname = hostname,
                ip = ip,
                score = score,
                ping = ping, 
                speed = speed, 
                country = country, 
                numVpnSessions = numVpnSessions,
                uptime = uptime,
                totalUsers = total_users,
                totalTraffic = total_traffic,
                log_type = log_type,
                config_data = config_data

            )

            vpn_pks.append( vpn.pk )
        
    print("VPN COUNT", models.VPN.objects.filter(pk__in = vpn_pks).count())
    models.VPN.objects.exclude(pk__in = vpn_pks).delete()
