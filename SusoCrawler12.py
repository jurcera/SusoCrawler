import urllib2
from BeautifulSoup import BeautifulSoup as Soup
import argparse

def completar_url(url_test):
    
    url_test = str(url_test.encode('utf-8'))
    
    if url_test.startswith("/"):
        url_test = dominio + url_test
    elif url_test.startswith("./"):
        url_test = dominio + url_test
        
    return url_test


parser = argparse.ArgumentParser(description ="Capturador de urls en Internet")
parser.add_argument('url', nargs =1, help='URL de busqueda. Debe ser del tipo http://www.suso.com')
parser.add_argument('-n', '--number-of-levels', type=int, default=1, help='Profundidad de busqueda')
args = parser.parse_args()
target_url = args.url.pop()
deep = args.number_of_levels

idx_deep = 1
dominio = target_url

user_agent = " Mozilla /5.0 ( X11; U; Linux x86_64 ; en-US) AppleWebKit /534.7 (KHTML , like Gecko ) Chrome/7.0.517.41 Safari /534.7 "
_opener = urllib2.build_opener()
_opener.addheaders = [( 'User-agent', user_agent )]
raw_code = _opener.open(target_url).read()

soup_code = Soup(raw_code)
links = [link['href'] for link
    in soup_code.findAll('a')
    if link.has_key('href')]

for url_check in links:
    url_ok = completar_url(url_check)
    print url_ok

