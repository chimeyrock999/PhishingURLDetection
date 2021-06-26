import csv
import urllib.request

reader = csv.DictReader(open("phising_url.csv"))

with open('phising_urls1.csv', 'w',  newline='') as csv_file:
    writer =csv.writer(csv_file)
    writer.writerow(['url'])
    for raw in reader:
        url=str(raw['url'])
        if( url.find('br')==-1 and url.find('ba')==-1):
            try:
                weburl=urllib.request.urlopen(url, timeout=0.75)
                if (int(weburl.getcode())>=200 and int(weburl.getcode())<300 ):
                    writer.writerow([url])
                    print(url)
            except Exception:
                print('failed')