from urllib.request import urlopen, urljoin
import re

def download_page(url):
    return urlopen(url).read().decode('utf-8')

def extract_image_links(page):
    link_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page)

if __name__ == '__main__':
    target_url = 'http://www.apress.com/'
    apress = download_page(target_url)
    image_links = extract_image_links(apress)

    for src in image_links:
        print(urljoin(target_url, src))