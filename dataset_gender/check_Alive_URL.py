import csv
import urllib.request

reader = csv.DictReader(open("benign_url1.csv"))

with open('benign_url2.csv', 'w',  newline='') as csv_file:
    writer =csv.writer(csv_file)
    writer.writerow(['url'])
    for raw in reader:
        try:
            url=raw['url']
            weburl=urllib.request.urlopen(url, timeout=0.75)
            if (int(weburl.getcode())>=200 and int(weburl.getcode())<300 ):
                writer.writerow([url])
                print(url)
        except Exception:
            print('failed')