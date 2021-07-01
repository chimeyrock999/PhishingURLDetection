from urllib import parse
from feature_extractor import extract
import whois
from datetime import datetime, timezone
import csv
import urllib.request


import feature_extractor
reader1 = csv.DictReader(open("urls-benign.csv"))

with open('benign_urls.csv', 'w',  newline='') as csv_file1:
    writer =csv.writer(csv_file1)
    writer.writerow(['url'])
    for raw in reader1:
        url=raw['url']
        print(url)
        try:
            link="https://www."+url
            weburl=urllib.request.urlopen(link, timeout=0.75)
            if (int(weburl.getcode())>=200 and int(weburl.getcode())<300 ):
                writer.writerow([link])
                print(link)
        except Exception:
            try:
                link="https://"+url
                weburl=urllib.request.urlopen(link, timeout=0.75)
                if (int(weburl.getcode())>=200 and int(weburl.getcode())<300 ):
                    writer.writerow([link])
                    print(link)
            except Exception:
                try:
                    link="http://www."+url
                    weburl=urllib.request.urlopen(link, timeout=0.75)
                    if (int(weburl.getcode())>=200 and int(weburl.getcode())<300 ):
                        writer.writerow([link])
                        print(link)
                except Exception:
                    try:
                        link="https://"+url
                        weburl=urllib.request.urlopen(link, timeout=0.75)
                        if (int(weburl.getcode())>=200 and int(weburl.getcode())<300 ):
                            writer.writerow([link])
                            print(link)
                    except Exception:
                        print('failed')