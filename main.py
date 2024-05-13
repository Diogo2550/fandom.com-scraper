import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse

"""
SOBRE: obtém todos os links de uma dada página de categoria do Fandom.com

O Fandom.com é dividido em algumas páginas que podem ser exploradas, sendo elas:
/wiki/Special:AllPages - todas as páginas da fandom
/wiki/Special:Categories - todas as categorias da fandom
/wiki/Category:{category} - todos as páginas da categoria escolhida

Atualmente atuamos na /Category:
"""

def run(fandom_url: str):
    url = urlparse(fandom_url)
    origin = url.scheme + '://' + url.hostname
    
    response = requests.get(fandom_url)
    body = response.text
    
    document = BeautifulSoup(body, 'html.parser')
    links = document.find_all('a', class_='category-page__member-link')
    
    return [ origin + link.get('href') for link in links ]