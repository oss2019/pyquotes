from fuzzywuzzy import fuzz, process
from bs4 import BeautifulSoup
import requests
import random

sleep_counter = 0

# Currently the API will have three functions.
# More functions to be added later.
# 1. Get the quote based on certain category and person
# 2. Get the quote of the day


def get_quotes(person: (None, str) = None,
               category: (None, str) = None):
    """
    This function returns all the quotes that matches the input.
    :param person:	 Name of the person e.g. Albert Einstein
    :param category: Category of quote e.g. Motivational
    :param return:   List of tuples [(quote, author_of_the_quote), ..]
    """
    return crawler(person, category)


def get_quote(person: (None, str) = None,
              category: (None, str) = None):
    """
    This function take a category and a person as a input and returns
    a random quote which matches the input.
    :param person:	 Name of the person e.g. Albert Einstein
    :param category: Category of quote e.g. Motivational
    :param return:   A tuple (quote, author_of_the_quote)
    """
    quotes_and_authors = crawler(person, category)
    if len(quotes_and_authors) > 1:
        index = random.randint(0, len(quotes_and_authors)-1)
    else:
        index = 0
    return quotes_and_authors[index]


def get_quote_of_the_day():
    """
    This fuction returns quote of the day.
    :param return: A tuple (quote, author_of_the_quote)
    """
    page_number = random.randint(1, 912)
    test = 1
    url = "https://api.quotery.com/wp-json/quotery/v1/quotes?orderby=popular&page=" + \
        str(page_number)+"&per_page=120"
    quote, authors, test = scraper(url, test)
    quotes_and_authors = selection_general(quote, authors)
    index = random.randint(0, len(quotes_and_authors)-1)
    return quotes_and_authors[index]


def scraper(url, test):
    authors = []
    quotes = []
    # Used a header to fake a browser
    source = requests.get(url, headers={
                          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}).text
    soup = BeautifulSoup(source, 'lxml')
    para = soup.p.text
    # all these random split is how the data was arranged in the source from which it had to be stripped
    para = para.split("\"quotes\"")
    if len(para) > 1:
        para = para[1]
    else:
        para = para[0]
    count = 0
    para = para.split("\"status\"")
    if len(para) == 1:
        para = para[0]
        quote_list = para.split("\"body\"")
        for index, element in enumerate(quote_list):
            quote_element = element.split("\"images\"")
            if index > 0:
                for inner_index, quote in enumerate(quote_element):
                    if inner_index == 0:
                        # Cleaning the quote and using the encode decode to remove Unicode escape chracters
                        cleaned_quote = quote[2:len(
                            quote)-2].encode('utf-8').decode('unicode-escape')
                        quotes.append(cleaned_quote)

        author_list = para.split("\"name\"")
        for index, element in enumerate(author_list):
            author_element = element.split("\"slug\"")
            if index > 0:
                for inner_index, author in enumerate(author_element):
                    if inner_index == 0:
                        # Cleaning the name of the author and using the encode decode to remove Unicode escape chracters
                        cleaned_author = author[2:len(
                            author)-2].encode('utf-8').decode('unicode-escape')
                        authors.append(cleaned_author)
                        count += 1
    else:
        test = 0
    return quotes, authors, test


def selection_author(quotes, authors, author):
    quotes_and_authors = []
    for i in range(len(quotes)):
        pair = (quotes[i], authors[i])
        if author == authors[i]:
            quotes_and_authors.append(pair)
        del pair
    return quotes_and_authors


def selection_general(quotes, authors):
    quotes_and_authors = []
    for i in range(len(quotes)):
        pair = (quotes[i], authors[i])
        quotes_and_authors.append(pair)
        del pair
    return quotes_and_authors


#def display_quotes(quotes_and_authors):
#    for tup in quotes_and_authors:
#        print(tup[0]+" - "+tup[1])
#        print('\n')


def crawler(user_author=None, user_topic=None):
    try:
        authors = []
        quote = []
        quotes_and_authors = []
        punctuations = (",", "-", "'", ".", '"', '_', '\\', '“', '”', '*')
        new_word = ""
        expected_author = []
        expected_topic = []

        file_topic = open('topics.txt', 'r')
        file_author = open('authors.txt', 'r')

        # Using FuzzyWuzzy to match input entry to the entries in the website. We are using text files from scrapped from the website for it.

        if user_topic != None:
            for topic in file_topic:
                clean_topic = topic[:-1]
                match = fuzz.token_set_ratio(user_topic, clean_topic)
                if match > 70:
                    expected_topic.append(clean_topic)
            if user_author != None:
                for author in file_author:
                    clean_author = author[:-1]
                    match = fuzz.token_set_ratio(user_author, clean_author)
                    if match > 90:
                        expected_author.append(clean_author)
                for topic in expected_topic:
                    topic = topic.lower()
                    for index, char in enumerate(topic):
                        if char not in punctuations:
                            new_word = new_word + char
                    new_word = '-'.join(new_word.split(" "))
                    i = 1
                    test = 1
                    while test:
                        url = ("https://api.quotery.com/wp-json/quotery/v1/quotes?topic="
                               + new_word + "&page=" + str(i) + "&per_page=120")
                        new_word = ""
                        i += 1
                        for author in expected_author:
                            quote, authors, test = scraper(url, test)
                            quotes_and_authors += selection_author(
                                quote, authors, author)
                        return quotes_and_authors
            else:
                # show random quotes from the topic
                i = 1
                test = 1
                while test:
                    for topic in expected_topic:
                        topic = topic.lower()
                        for index, char in enumerate(topic):
                            if char not in punctuations:
                                new_word = new_word + char
                        new_word = '-'.join(new_word.split(" "))
                        url = ("https://api.quotery.com/wp-json/quotery/v1/quotes?topic="
                               + new_word + "&page=" + str(i) + "&per_page=120")
                        new_word = ""
                        i += 1
                        quote, authors, test = scraper(url, test)
                        quotes_and_authors += selection_general(quote, authors)
                return quotes_and_authors
        else:
            if user_author != None:
                for author in file_author:
                    clean_author = author[:-1]
                    match = fuzz.token_set_ratio(user_author, clean_author)
                    if match > 90:
                        expected_author.append(clean_author)
                for author in expected_author:
                    i = 1
                    test = 1
                    author = author.lower()
                    for index, char in enumerate(author):
                        if char not in punctuations:
                            new_word = new_word + char
                    new_word = '-'.join(new_word.split(" "))
                    while test:
                        url = ("https://api.quotery.com/wp-json/quotery/v1/quotes?author="
                               + new_word + "&page=" + str(i) + "&per_page=120")
                        i += 1
                        quote, authors, test = scraper(url, test)
                        quotes_and_authors += selection_general(quote, authors)
                    new_word = ""
                    return quotes_and_authors
            else:
                # Too Few Arguments. Throw random quotes>?
                pass

    except requests.exceptions.ConnectionError as e:
        pass


# #Test for Quote of The Day
# print(get_quote_of_the_day())
# #Test for get_quotes()
# print(get_quotes("Zoe Saldana",None))
# #Test for get_quote()
# print(get_quote("Robert Downey Jr.",None))
