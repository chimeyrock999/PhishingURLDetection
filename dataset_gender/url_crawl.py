from bs4 import BeautifulSoup
import urllib.request
import csv

with open('phising_url.csv', 'w', newline='') as csv_file:
    writer =csv.writer(csv_file)
    for page in range (97,156):
        url ="http://phishtank.org/phish_search.php?page="+str(page)+"&active=y&valid=y&Search=Search"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        urls = soup.find_all('td', class_="value")
        for u in urls:
            t=str(u.text)
            try:
                int(t)
            except Exception:
                if (t!='VALID PHISH' and t!='ONLINE'):
                    if( t.find('by')==-1):
                        start=len(t)-t.find('added')
                        t=t[:-start]
                        if (t!=''):
                            print(t)
                            writer.writerow([t])