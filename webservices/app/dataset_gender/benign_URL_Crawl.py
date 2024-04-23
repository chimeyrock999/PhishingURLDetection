from bs4 import BeautifulSoup
import urllib.request
import csv

with open('benign_urls.csv', 'w', newline='') as csv_file1:
    writer =csv.writer(csv_file1)
    for page in range (1,800):
        print(page)
        url ="http://phishtank.org/phish_search.php?page="+str(page)+"&active=n&valid=n&Search=Search"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        urls = soup.find_all('td', class_="value")
        for u in urls:
            t=str(u.text)
            try:
                id=int(t)
            except Exception:
                if (t!='INVALID' and t!='Offline'):
                    if( t.find('by')==-1):
                        #start=len(t)-t.find('added')
                        #t=t[:-start]
                        if( t.find('...')==-1):
                            start=len(t)-t.find('added')
                            t=t[:-start]
                            print(t)
                            print(page)
                            writer.writerow([t])