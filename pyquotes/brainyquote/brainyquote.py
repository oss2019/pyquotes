import requests
from bs4 import BeautifulSoup
import html5lib  # Html Parser
import re
import random

# This function returns the link to be scraped for the author.
# For example if the author is Bill Gates then url at brainyquote
# will be "https://www.brainyquote.com/authors/bill_gates"


def get_author_link(person):
    author_name = person.lower()
    author_name_split = author_name.split(' ')
    author_url_link = ''
    count = 0

    for i in author_name_split:
        author_url_link += i
        count += 1
        if count is not len(author_name_split):
            author_url_link += '_'

        author_url_link = author_url_link.replace('.', '_')

    return author_url_link


def get_quotes(person, category):
    """
    This function returns all the quotes that matches the input.

    :param person:   Name of the person e.g. Albert Einstein
    :param category: Category of quote e.g. Motivational
    :param return:   List of tuples [(quote, author_of_the_quote), ..]
    """
    URL = 'https://www.brainyquote.com/authors/' + get_author_link(person)
    respone_author = requests.get(URL)
    soup_author = BeautifulSoup(respone_author.content, 'html5lib')
    categories = soup_author.find_all('div', class_='kw-box')
    check = False
    count = 0
    for i in categories:
        a = i.text
        replace = a.replace('\n', '')
        r = replace.lower()
        if category in r:
            check = True
            count += 1

    # Getting the quote of the related author
    get_quote = soup_author.find_all('a', attrs={'title': 'view quote'})
    quote_list = []
    big_list = []
    for i in range(count):
        quote_list.append((get_quote[i].text, person))
        big_list.append(quote_list)

    if len(quote_list) == 0:
        return('''Oops! It seems that there are no quotes of the author of that
                category.
                \nYou may consider changing the category or the author ''')

    return(quote_list)


def get_quote(person, category):
    """
    This function take a category and a person as a input and returns
    a random quote which matches the input.

    :param person:   Name of the person e.g. Albert Einstein
    :param category: Category of quote e.g. Motivational
    :param return:   A tuple (quote, author_of_the_quote)
    """
    quotes = get_quotes(person, category)
    length = len(quotes)
    if(length == 0):
        # In case no quote of the author exist for that category.
        return('No quotes found of that category')
    else:
        random_number = random.randint(0, length - 1)
        quote_with_author_list = []
        quote_with_author_list.append(quotes[random_number])
        quote_with_author_list.append(person)

        return(tuple(quote_with_author_list))


def get_quote_of_the_day():
    """
    This fuction returns quote of the day.

    :param return: A tuple (quote, author_of_the_quote)
    """
    URL = 'https://www.brainyquote.com/quote_of_the_day'

    # Sending a HTTP request to the specified URL and saving the response
    # from server in a response object called response.
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html5lib')
    a_tags = soup.findAll('img', alt=True)

    # Getting all the a tags of the page.
    quote_of_the_day_atag = str(a_tags[0])

    # Grabbing the first a tag of the page
    matches = re.findall(r'\"(.+?)\"', quote_of_the_day_atag)

    # A regular expression which gives a list of all
    # text that is in between quotes.
    quote_author_split_list = str(matches[0]).split('-')

    #  Get a list of quote_of_the_day and the author
    quote_of_the_day = matches[0].replace(quote_author_split_list[-1], '')
    quote_of_the_day = quote_of_the_day.replace('-', '')
    author_name = quote_author_split_list[-1]

    # Gives the author_name
    author_name = author_name.replace(' ', '')

    # Removes any extra space
    return (quote_of_the_day, author_name)
