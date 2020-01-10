from urllib.request import urlopen, urljoin
import re

def download_page(url):
    return urlopen(url).read().decode('utf-8')

def extract_links(page):
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page)

if __name__ == '__main__':
    target_url = "https://ls.sir.sportradar.com/future/en?fbclid=IwAR3W0CRBFmuDsY2D2ZiU-ARWb-uAV5TfOd5gwR6BkglkPxNM2NPqf0-xEEU"
    sportradar = download_page(target_url)
    links = extract_links(sportradar)

    for link in links:
        print(urljoin(target_url, link))