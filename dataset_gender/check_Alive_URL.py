import csv
import urllib.request

reader1 = csv.DictReader(open("benign_url.csv"))

with open('benign_urls.csv', 'w',  newline='') as csv_file1:
    writer =csv.writer(csv_fil1)
    writer.writerow(['url'])
    for raw in reader1:
        try:
            url=raw['url']
            weburl=urllib.request.urlopen(url, timeout=0.75)
            if (int(weburl.getcode())>=200 and int(weburl.getcode())<300 ):
                writer.writerow([url])
                print(url)
        except Exception:
            print('failed')

reader2 = csv.DictReader(open("phising_url.csv"))

with open('phising_urls.csv', 'w',  newline='') as csv_file2:
    writer =csv.writer(csv_file2)
    writer.writerow(['url'])
    for raw in reader2:
        url=str(raw['url'])
        if( url.find('br')==-1 and url.find('ba')==-1):
            try:
                weburl=urllib.request.urlopen(url, timeout=0.75)
                if (int(weburl.getcode())>=200 and int(weburl.getcode())<300 ):
                    writer.writerow([url])
                    print(url)
            except Exception:
                print('failed')