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
    urls = ["https://www.dropbox.com/sm/password?cont=https://www.dropbox.com/s/hf4...",
                "https://www.dropbox.com/sm/password?cont=https://www.dropbox.com/s/hf4...",
                "https://www.liputan6.com/bola/read/4204683/blaise-matuidi-positif-coro...",
                "https://cheerseeftapps.com/feed/posts/many-women-saw-kavanaugh-wrongly...",
                "http://cheerseeftapps.com/feed/posts/many-women-saw-kavanaugh-wrongly-...",
                "https://www.youtube.com/watch?v=_TWbWzhJ2dM&ab_channel=TheHanoiChamomile"
            ]
    d2 = datetime.now()
    for url in urls:
        features =[]
        features = extract.extract_new_url(url)
        print(features)
        

if __name__ == "__main__":
    main()
