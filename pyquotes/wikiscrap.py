from bs4 import BeautifulSoup
import requests

source = requests.get("https://en.wikiquote.org/wiki/Main_Page").text
soup  = BeautifulSoup(source,"lxml")
#names is  list of all names with links in the main page of wikiquote
names = soup.find('div',class_='mw-parser-output').find_all('div')[11].find_all('p')[1].find_all('a')

def get_quotes(person):
    quotes_by_author = list()
    for name in names:
        if (person == name.text.lower()):
            link = "https://en.wikiquote.org" + name['href']
            link = requests.get(link).text
            soup_for_indiv = BeautifulSoup(link,"lxml")
            quotes = soup_for_indiv.find_all('div',class_='mw-parser-output')[0].find_all('ul')
            for quote in quotes:
                try:
                    if (quote.li.b==None):                  #if there is no quote
                        continue
                    elif quote.li.b.text.isdigit()==True:   #so that there aren't any numbers
                        continue
                    elif len(quote.li.b.text.split(' '))<2: #so that there aren't any words
                        continue    
                    else:
                        temp = [quote.li.b.text,name.text]
                        quotes_by_author.append(tuple(temp))
                except:
                    continue
        else:
            continue
    return quotes_by_author

#scrapping for quote of the day
path_for_quote_of_the_day = soup.find_all('table')[2].find_all('tbody')[2].find_all('tr')
quote_of_the_day = path_for_quote_of_the_day[0].td.text
author_for_quote_of_the_day = path_for_quote_of_the_day[1].td.a.text
quote_of_the_day_tuple = (quote_of_the_day.rstrip(),author_for_quote_of_the_day) 

def get_quote_of_the_day():
    return quote_of_the_day_tuple

