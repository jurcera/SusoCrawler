import urllib2
from BeautifulSoup import BeautifulSoup as Soup
import argparse

user_agent = " Mozilla /5.0 ( X11; U; Linux x86_64 ; en-US) AppleWebKit /534.7 (KHTML , like Gecko ) Chrome/7.0.517.41 Safari /534.7 "
_opener = urllib2.build_opener()
_opener.addheaders = [( 'User-agent', user_agent )]
raw_code = _opener.open("http://www.google.es/").read()

soup_code = Soup(raw_code)
links = [link['href'] for link
    in soup_code.findAll('a')
    if link.has_key('href')]

print links

parser = argparse.ArgumentParser(description ="Capturador de urls en Internet")
parser.add_argument('url', nargs =1, help='URL destino')
parser.add_argument('-n', '--number-of-levels', type=int, default=1, help='Profundidad de busqueda')
args = parser.parse_args()
target_url = args.url.pop()
deep = args.number_of_levels
print target_url
print deep
