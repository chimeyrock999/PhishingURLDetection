import argparse
from feature_extractor import extract
import whois
from datetime import datetime, timezone

import feature_extractor


def check_time_activation_domain(url):
    try:
        result_whois = whois.whois(url)
        if not result_whois:
            return '?'
        creation_date = str(result_whois.creation_date)
        formated_date = " ".join(creation_date.split()[:1])
        d1 = datetime.strptime(formated_date, "%Y-%m-%d")
        d2 = datetime.now()
        return abs((d2 - d1).days)
    except Exception:
        return 'false'

def main():
    urls = ["https://www.lewisrallysport.com/virtual/?generatecode=gabrieldaarte@yahoo.com.br",
            "https://dbs.mc.eu1.kontiki.com/global2/content?entity=31321&moid=1eeef761-d931-4219-886a-5b467413620d",
            "http://dbs.mc.eu1.kontiki.com/global2/content?entity=31321&moid=1eeef761-d931-4219-886a-5b467413620d",
            "http://www.bergenfamiilycenter.org/yahoo-login=yahoo-mail-update-comm-yahoo=update-yahoo=mail-yahoo-update=yah00-mail=update-mail-yaho0=mail-login=yahoo-mail=login-yah00=mail/",
            ]
    d2 = datetime.now()
    for url in urls:
        features =[]
        features = extract.extract_new_url(url)
        print(features)
        

if __name__ == "__main__":
    main()