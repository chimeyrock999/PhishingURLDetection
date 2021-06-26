import argparse
from feature_extractor import extract


def main():
    urls = ["http://arnozom.co.ip.zspqpft.asia/", 
            "https://firebasestorage.googleapis.com/v0/b/absupdate-89af2.appspot.co...",
            "https://authentic0000-authetical00000.web.app/#aaaa@example.jp...",
            "https://treasurerproperty.com/customersupport/login_auth.php?onlineid=...",
            "https://www.youtube.com/watch?v=sca4VG9b0NY&ab_channel=Abao%E1%BB%9FTokyoAbao%E1%BB%9FTokyo"
            ]
    for url in urls:
        feature= []
        feature = extract.extract_new_url(url)
        print(feature)

if __name__ == "__main__":
    main()
