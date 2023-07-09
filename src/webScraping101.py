import requests
from requests import Response
from bs4 import BeautifulSoup


def getData(uri: str):
    response: Response = requests.get(uri)
    siteHTML = BeautifulSoup(response.text,"html.parser")
    return siteHTML

def parseHTML(siteHTML):
    quotes = siteHTML.findAll('span',attrs={'class':'text'})
    authors = siteHTML.findAll('small',attrs={
        'class':'author'
    })
    return (quotes, authors)

def main():
    uri = 'https://quotes.toscrape.com/'
    siteHTML = getData(uri)
    quotes, authors = parseHTML(siteHTML)

    for index, quote in enumerate(quotes):
        print(index, quote, '\n')

    for index, author in enumerate(authors):
        print(index, author, '\n')


if __name__ == '__main__':
    main()