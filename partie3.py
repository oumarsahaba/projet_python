import requests
from bs4 import BeautifulSoup
import re
  
def get_page(url):
    """prend en entrée une url et retourne le contenu de la page en chaine"""
    page = requests.get(url)
    content = str(BeautifulSoup(page.content, 'html.parser'))
    return content

def get_emails(url):
    email_pattern=r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    content=get_page(url)
    return re.findall(email_pattern,content)

def get_urls(url):
    """retourne la liste des url de cette page"""
    pattern_url=r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    content=get_page(url)
    return re.findall(pattern_url,content)

def get_tables(url):
    """retourne une liste de code html des codes de la page"""
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser').find_all("table")
    return content


if __name__ == '__main__':
    get_page('https://pythex.org/')
    