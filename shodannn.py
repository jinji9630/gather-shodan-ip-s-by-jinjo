import shodan


ports=[8081,8000,443,8181,8001,8002,8083,8085,9001,8880,80,9000,8089,18080,9200,9002,3001,9091,10443,5001,8009,6000,8889,9095,6443,5000,8899,9999,25,7001,10000,8443,30718,31022,777,4444,85000,30422,14265,30303,53,465,9898, 587,
    6379,
    9100,
    51235,
    1337,
    445,
    5006,
    7071,
    8333,
    18081,
    21,
    1081,
    8140,
    9443,
    311,
    1080,
    2082,
    2086,
    28080,
    31322,
    50000,
    2077,
    3780,
    4433,
    11300,
    60001,
    137,
    873,
    3389,
    4000,
    7443,
    8080,
    8888,
    9306,
    444,
    1023,
    1024,
    2083,
    2095,
    2096,
    4443,
    5555,
    5601,
    5901,
    6002,
    7434,
    8087,
    8139,
    8200,
    8545,
    9201,
    9203,
    9333,
    9530,
    9943,
    9944,
    17000,
    22222,
    22556,
    27015,
    30002,
    30222,
    30301,
    38333,
    49152,
    49153,
    52869,
    6002]

i=0
SHODAN_API_KEY = ["fcXCsZhGgkYBon1zmlG06GQGhbZ50aAm","pBDzKU5gaoiMnjgkzC4IjG9Zgvit70bH"]
for port in ports:
    i=i+1
    api = shodan.Shodan(SHODAN_API_KEY[i%2])


    shodan_ips=open("shodan_ips.txt","w")
    array_ips=[]
    try:
        results = api.search('laravel port:8081',page=1)
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            array_ips.append(result['ip_str'])
            shodan_ips.write(result['ip_str']+"\n")
            print('')
            print(len(array_ips))
            if(len(array_ips) == 100):
                results = api.search('laravel port:8081',page=2)
                for result in results['matches']:
                    print('IP: {}'.format(result['ip_str']))
                    array_ips.append(result['ip_str'])
                    shodan_ips.write(result['ip_str']+"\n")
    except:
        print('error')
