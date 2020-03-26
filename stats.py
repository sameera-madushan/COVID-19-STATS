import requests
import re

def all():
    url = "https://corona.lmao.ninja/all"
    t = requests.get(url).json()
    print("Global Stats")
    for k,v in t.items():
        if k == "updated":
            continue
        _key = str(k).capitalize()
        _value = str(v).capitalize()
        print(" "+ _key + ":" + _value, end='')

print(r'''
  ___  __   _  _  __  ____        __  ___     ____  ____  __  ____  ____ 
 / __)/  \ / )( \(  )(    \ ___  /  \/ _ \   / ___)(_  _)/ _\(_  _)/ ___)
( (__(  O )\ \/ / )(  ) D ((___)(_/ /\__  )  \___ \  )( /    \ )(  \___ \
 \___)\__/  \__/ (__)(____/      (__)(___/   (____/ (__)\_/\_/(__) (____/
    Track COVID-19 stats from command line          [Sameera Madushan]
''')

all()

def allcountries():
    url = "https://corona.lmao.ninja/countries"
    t = requests.get(url).json()

    print ("{:<25} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Country', 'Cases', 'TodayCases', 'Deaths', 'TodayDeaths', 'Recovered', 'Critical', 'CasesPerOneMillion') + "\n") 
    for i in t:
        a = str(i['country'])
        b = str(i['cases'])
        c = str(i['todayCases'])
        d = str(i['deaths'])
        e = str(i['todayDeaths'])
        f = str(i['recovered'])
        g = str(i['critical'])
        h = str(i['casesPerOneMillion'])

        print ("{:<25} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(a, b, c, d, e, f, g, h))

def sort(x):
    url = ("https://corona.lmao.ninja/countries?sort={}").format(x)
    t = requests.get(url).json()

    print ("{:<25} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Country', 'Cases', 'TodayCases', 'Deaths', 'TodayDeaths', 'Recovered', 'Critical', 'CasesPerOneMillion') + "\n") 
    for i in t:
        a = str(i['country'])
        b = str(i['cases'])
        c = str(i['todayCases'])
        d = str(i['deaths'])
        e = str(i['todayDeaths'])
        f = str(i['recovered'])
        g = str(i['critical'])
        h = str(i['casesPerOneMillion'])

        print ("{:<25} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(a, b, c, d, e, f, g, h))

def country(y):
    url = ("https://corona.lmao.ninja/countries/{}?strict=true").format(y)
    req = requests.get(url).content.decode('utf-8')
    if req:
        check = re.search(r'Country not found',req)
        if check:
            print("Country not found")
        else:
            _p = requests.get(url).json()
            for k, v in _p.items():
                if k == 'countryInfo':
                    continue
                i = str(k).capitalize()
                # print(str(k) + "\n" + str(v))  
                print('{:<25} {:<10}'.format(i, str(v)))
    else:
        print("error")

def getCountry():
    print("\n")
    my_ip = requests.get("https://ident.me/").content.decode("UTF-8")
    url = ("https://api.hackertarget.com/geoip/?q={}").format(my_ip)
    result = requests.get(url).content.decode('utf-8')
    search = re.search(r'Country: (.*)',result).group(1)
    print("\nIt looks like you are in {}.".format(search))
    print("Here are the stats related to your country. (If this prediction is incorrect use option \"3\")\n")
    country(y=search)

getCountry()

try:
    print(("\nPress \"1\" to list stats related to all countries.\nPress \"2\" to sort countries list according to a given key.\nPress \"3\" to check stats realated to your country."))
    x = int(input(">"))
    if x == 1:
        allcountries()
    if x == 2:
        print("\nSelect any key to sort")
        print("Keys:- Country, Cases, Active, Critical, Deaths, Recovered, TodayCases, TodayDeaths, CasesPerOneMillion\n")
        y = str(input(">")).lower()
        if y == "country":
            sort(x=y)
        if y == "cases":
            sort(x=y)
        if y == "active":
            sort(x=y)
        if y == "critical":
            sort(x=y)
        if y == "deaths":
            sort(x=y)
        if y == "recovered":
            sort(x=y)
        if y == "todaycases":
            sort(x=y)
        if y == "todaydeaths":
            sort(x=y)
        if y == "casesperonemillion":
            sort(x=y)

    if x == 3:
        t = str(input("\nEnter your country name: "))
        print("\n", end='')
        country(y=t)
     
except KeyboardInterrupt:
    print("\nProgramme Interrupted")
