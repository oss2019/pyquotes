from bs4 import BeautifulSoup
import requests

source = requests.get("https://en.wikiquote.org/wiki/Main_Page").text
soup = BeautifulSoup(source, "lxml")
# names is  list of all names with links in the main page of wikiquote
names_path = soup.find('div', class_='mw-parser-output').find_all('div')[11]
names = names_path.find_all('p')[1].find_all('a')


def get_quotes(person):
    quotes_by_author = list()
    for name in names:
        if (person == name.text.lower()):
            link = "https://en.wikiquote.org" + name['href']
            link = requests.get(link).text
            soup_for_indiv = BeautifulSoup(link, "lxml")
            q = soup_for_indiv.find_all('div', class_='mw-parser-output')[0]
            quotes = q.find_all('ul')
            for quote in quotes:
                try:
                    if quote.li.b is None:
                        continue
                    elif quote.li.b.text.isdigit():
                        continue
                    elif len(quote.li.b.text.split(' ')) < 2:
                        continue
                    else:
                        temp = [quote.li.b.text, name.text]
                        quotes_by_author.append(tuple(temp))
                except:
                    continue
        else:
            continue
    return quotes_by_author

# scrapping for quote of the day
path_0_for_quote_of_the_day = soup.find_all('table')[2].find_all('tbody')[2]
path_for_quote_of_the_day = path_0_for_quote_of_the_day.find_all('tr')
quote_of_the_day = path_for_quote_of_the_day[0].td.text
author_for_quote_of_the_day = path_for_quote_of_the_day[1].td.a.text


def get_quote_of_the_day():
    return (quote_of_the_day, author_for_quote_of_the_day)

