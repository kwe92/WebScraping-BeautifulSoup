import requests
import pandas as pd
from requests import Response
from bs4 import BeautifulSoup, ResultSet


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

    quotesText = []
    authorsText = []

    for quote, author in zip(quotes, authors):
        quotesText.append(quote.text)
        authorsText.append(author.text)
    quotesData = {'authors': authorsText,
            'quotes': quotesText}
    
    quotesDataFrame = pd.DataFrame(data=quotesData)
    quotesDataFrame['quotes'] = quotesDataFrame['quotes'].apply(lambda x: x.replace('"',''))
    quotesDataFrame.to_excel('quotesData.xlsx', index=False)

    print('DATA SAVED SUCCESSFULLY')

    # print(quotesDataFrame)


    # printQuotes(quotes, authors)

    # print('\n')

if __name__ == '__main__':
    main()