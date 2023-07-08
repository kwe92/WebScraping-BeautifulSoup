import requests
from requests import Response
from bs4 import BeautifulSoup


uri = 'https://quotes.toscrape.com/'

def getData(uri: str):
    response: Response = requests.get(uri)
    siteHTML = BeautifulSoup(response.text,"html.parser")
    return siteHTML

def parseHTML(getDataCallback: function, criterion: dict):
    tag: list = criterion['tag']
    atters: dict = criterion['attrs']
    pass

def main():
    pass

if __name__ == '__main__':
    main()