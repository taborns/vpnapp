import csv 
from vpn import models 

def scrapVPNS(url):
    with open(url) as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        vpn_pks = []

        for row in csv_reader:
            line_count += 1

            if line_count < 3 or len(row) != 15:
                print("LEN", len(row))
                continue
            else:
                print("I AM HERES")
                hostname, ip, score, ping, speed, country, country_short, numVpnSessions, uptime, total_users, total_traffic, log_type, operator, message, config_data = row 
                try:
                    country = models.Country.objects.get(short=country_short)
                except:
                    country = models.Country.objects.create(name=country, short=country_short)
                print(ping)
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
                    operator = operator,
                    config_data = config_data

                )

                vpn_pks.append( vpn.pk )
            
        
        models.VPN.objects.exclude(pk__in = vpn_pks).delete()


        
        print(f'Processed {line_count} lines.')
