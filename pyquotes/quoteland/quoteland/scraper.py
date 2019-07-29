from bs4 import BeautifulSoup
import requests
import random

# website used :
parent_link = "https://www.quoteload.com"

# for quote of the day :
day_quote = "https://www.brainyquote.com/quote_of_the_day"


def get_quotes(person: (None, str) = None, category: (None, str) = None):
    """
        usage : call with person name and category of quotes
        returns : a list of tuple (quote,author)
    """
    # function called without any argument:
    if person is None and category is None:
        # function called without any argument:
        print("too few arguments to get quotes")
        return None  # can be modified to throw some exception instead

    result = []
    if person is not None:  # person's name is provided
        # formatting the name to fit as per URL
        Person = "-".join(person.strip().split())
        person_link = requests.get(
            parent_link + "/quotes/authors/" + Person).text
        soup_obj = BeautifulSoup(person_link, "lxml")
        for interest in soup_obj.find_all("div", class_="card-body text-center"):
            quote = interest.p.find("a", class_="href-noshow").text
            tag = interest.p.find("a", class_="category-tag").text
            result.append((quote, person))

    if category is not None: 
         # category's name is provided
        category_link = requests.get(
            parent_link + "/quotes/categories/" + category
        ).text
        soup_obj = BeautifulSoup(category_link, "lxml")

        for interest in soup_obj.find_all("div", class_="card-body text-center"):
            quote = interest.p.find("a", class_="href-noshow").text
            tag = interest.p.find("a", class_="category-tag").text
            author = interest.p.find("a", class_="quote-author").text
            if (quote, author) not in result:
                result.append((quote, author))

    return result  # a list of tuples


def get_quote(person: (None, str) = None, category: (None, str) = None):
    lst = get_quotes(person=person, category=category)
    # error will be handled when list is empty (codes for the same to be added
    # soon)
    return lst[random.randint(0, len(lst))]


def random_quote():
    """
        usage : call without arguments
        returns : tuple of random quote,author
    """
    link = requests.get(day_quote).text
    soup_obj = BeautifulSoup(link, "lxml")
    for interest in soup_obj.find_all("div", class_="clearfix"):
        quote = interest.find("a", title="view quote").text
        author = interest.find("a", title="view author").text
        # return (quote, author)
        return (quote, author)


# print(get_quote(person="mahatma gandhi",category="legal"))
# print(get_quote(input('enter the name : ').strip()))

# print(random_quote())
