# Currently the API will have two functions.
# More functions to be added later.
# 1. Get the quote based on certain category and person
import requests
from bs4 import BeautifulSoup
import random


def get_quotes(person: (None, str) = None,
               category: (None, str) = None):
    """
    This function returns all the quotes that matches the input.

    :param person:	 Name of the person e.g. Albert Einstein
    :param category: Category of quote e.g. Motivational
    :param return:   List of tuples [(quote, author_of_the_quote), ..]

    """
    scrape_url = "https://www.curatedquotes.com/topic/"
    url_raw_data = requests.get(scrape_url)
    data = url_raw_data.text
    
    #checks for category in all categories 
    soup=BeautifulSoup(data,'html5lib')
    categories=[]
    for tag in soup.findAll('div',attrs={'class':"topics"}):
        if tag.findAll('a',href=True)!= None:
            for element in tag.findAll('a',href=True):
                print(element.text.strip())
                categories.append(element.text.strip())

    if category not in categories:
        return quotes_list

    #in all the quotes pf that category it searches for author 

    else:
        scrape_url='https://www.curatedquotes.com'
        for tag in soup.findAll('div',attrs={'class':"topics"}):
            if tag.findAll('a',href=True)!= None:
                for element in tag.findAll('a',href=True) :
                    if element.text.strip()==category:
                        scrape_url+=element["href"]
                        break

        url_raw_data = requests.get(scrape_url)
        data = url_raw_data.text
        soup=BeautifulSoup(data,'html5lib')
        for block in soup.findAll('blockquote'):
            quotes.append(block.p.text.strip())

        quotes_list=[]
        print(len(quotes))
        for quote in quotes:
            ls=quote.split('.')
            if len(ls)<2:
                continue
            if quote.find(person)!=-1:
                for i in range(len(ls)-1):
                    quote+=ls[i]

                quotes_list.append((person,quote))

        return quotes_list
    


def get_quote(person: (None, str) = None,
              category: (None, str) = None):
    """
    This function take a category and a person as a input and returns
    a random quote which matches the input.

    :param person:	 Name of the person e.g. Albert Einstein
    :param category: Category of quote e.g. Motivational
    :param return:   A tuple (quote, author_of_the_quote)
    """

    quotes = get_quotes(person, category)
    length = len(quotes)
    if(length == 0):
        # In case no quote of the author exist for that category.
        return("No such quote found for the author in that category")
    else:
        random_number = random.randint(0, length - 1)

    return quotes[random_number]




