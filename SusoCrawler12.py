#! /usr/bin/python
# coding=UTF-8


import urllib2
from BeautifulSoup import BeautifulSoup as Soup
import argparse

def descargar_html(target_url):

    user_agent = " Mozilla /5.0 ( X11; U; Linux x86_64 ; en-US) AppleWebKit /534.7 (KHTML , like Gecko ) Chrome/7.0.517.41 Safari /534.7 "
    _opener = urllib2.build_opener()
    _opener.addheaders = [( 'User-agent', user_agent )]
    raw_code = _opener.open(target_url).read()
    
    return raw_code

def extraer_enlaces(codigo_html):
    soup_code = Soup(codigo_html)

    links = [link['href'] for link
        in soup_code.findAll('a')
        if link.has_key('href')]
    
    return links

def crawler_url(url_to_check,idx_deep):
    while idx_deep <= deep:
        idx_deep = idx_deep + 1
        codigo_fuente = descargar_html(url_to_check)
        enlaces = extraer_enlaces(codigo_fuente)
        for enlace in enlaces:
            if enlace.startswith("/"):
                enlace = url_to_check + enlace
            elif enlace.startswith("#"):
                enlace = "novalido"
            
            if enlace != "novalido":
                print str(idx_deep-1) + " " + enlace
                crawler_url(enlace,idx_deep)

             
parser = argparse.ArgumentParser(description ="Capturador de urls en Internet")
parser.add_argument('url', nargs =1, help='URL de busqueda. Debe ser del tipo http://www.suso.com')
parser.add_argument('-n', '--number-of-levels', type=int, default=1, help='Profundidad de busqueda')
args = parser.parse_args()
target_url = args.url.pop()
deep = args.number_of_levels

idx_deep = 1
url_to_check = target_url
   
crawler_url(url_to_check,idx_deep)

