import requests
from requests import Response
from bs4 import BeautifulSoup


def getData(uri: str):
    response: Response = requests.get(uri)
    siteHTML = BeautifulSoup(response.text,"html.parser")
    return siteHTML

def parseHTML(siteHTML):
    quotes = siteHTML.findAll("span",attrs={'class':'text'})
    return quotes

def main():
    uri = 'https://quotes.toscrape.com/'
    siteHTML = getData(uri)
    print(parseHTML(siteHTML))

if __name__ == '__main__':
    main()