from bs4 import BeautifulSoup
import requests
import random

# website used :
parent_link = "https://www.quoteload.com"
# for quote of the day :
day_quote = "https://www.brainyquote.com/quote_of_the_day"


def get_quotes(person: (None, str) = None, category: (None, str) = None):
    # function called without any argument:
    if isinstance(person, type(None)) and isinstance(category, type(None)):
        print('too few arguments to get quotes')
        return None  # can be modified to throw some exception instead

    result = []
    if not isinstance(person, type(None)):  # person's name is provided
        # formatting the name to fit as per URL
        Person = "-".join(person.strip().split())
        person_link = requests.get(
            parent_link + "/quotes/authors/" + Person).text
        soup_obj = BeautifulSoup(person_link, 'lxml')
        for interest in soup_obj.find_all("div", class_="card-body text-center"):
            quote = interest.p.find('a', class_="href-noshow").text
            tag = interest.p.find('a', class_="category-tag").text
            result.append((quote, person))

    if not isinstance(category, type(None)):  # category's name is provided
        category_link = requests.get(
            parent_link + "/quotes/categories/" + category).text
        soup_obj = BeautifulSoup(category_link, 'lxml')

        for interest in soup_obj.find_all("div", class_="card-body text-center"):
            quote = interest.p.find('a', class_="href-noshow").text
            tag = interest.p.find('a', class_="category-tag").text
            author = interest.p.find('a', class_="quote-author").text
            if (quote, author) not in result:
                result.append((quote, author))

    return result  # a list of tuples


def get_quote(person: (None, str) = None, category: (None, str) = None):
    lst = get_quotes(person=person, category=category)
    return lst[random.randint(0, len(lst))]


def quote_of_the_day():
    link = requests.get(day_quote).text
    soup_obj = BeautifulSoup(link, 'lxml')
    quote = soup_obj.find('div', class_='clearfix').find(
        'a', title='view quote').text
    author = soup_obj.find('div', class_='clearfix').find(
        'a', title='view author').text
    return (quote, author)


# print(get_quote(person="mahatma gandhi",category="legal"))
print(quote_of_the_day())
