import requests
from requests import Response
from bs4 import BeautifulSoup, ResultSet, Tag


def getData(uri: str):
    response: Response = requests.get(uri)
    siteHTML: BeautifulSoup = BeautifulSoup(response.text,"html.parser")
    return siteHTML

def parseHTML(siteHTML):
    quotes: ResultSet = siteHTML.findAll('span',attrs={'class':'text'})
    authors: ResultSet = siteHTML.findAll('small',attrs={
        'class':'author'
    })
    return (quotes, authors)

def printQuotes(quotes: ResultSet, authors: ResultSet):
    print(f'\ntype quotes: {type(quotes)}\n')
    for quote, author in zip(quotes, authors):
        print(f'''
{quote.text}

    - {author.text}
''', '\n')

def main():
    uri = 'https://quotes.toscrape.com/'
    siteHTML = getData(uri)
    quotes, authors = parseHTML(siteHTML)

    printQuotes(quotes, authors)

    print('\n')

if __name__ == '__main__':
    main()