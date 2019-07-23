import requests
from bs4 import BeautifulSoup
import random


def get_quotes(category):
    """
    This function returns all the quotes that matches the input.
    :param category: Category of quote e.g. Motivational
    :param return:   List of tuples [(quote, author_of_the_quote), ..]
    """
    # Sending a HTTP request and saving the response
    # from server in a response object called response.
    response = requests.post('http://www.powerquotes.net/search_results.asp',
                             data={'search_word': category})
    soup = BeautifulSoup(response.text, 'lxml')
    # Grabbing first table in variable table
    table = soup.find('table')

    # Grabbing all tables inside table
    list_table = table.find_all('table')

    # Grabbing all quotes in variable list_paragraph_tag
    list_paragraph_tag = list_table[2].find_all('p')
    quote_list = []
    del list_paragraph_tag[0]

    if len(list_paragraph_tag) <= 1:
        # In case no quote exis for that category
        return('''Oops! It seems that there are no quotes for that
                category.
                \nYou may consider changing the category ''')
    else:
        for j in range(2):
            del list_paragraph_tag[len(list_paragraph_tag)-1]
        for i in list_paragraph_tag:
            a = i.text
            replace = a.replace("\'", '')
            replace = replace.replace("\xa0\xa0", " ")
            replace = replace.replace("\xa0", " ")
            quote_list.append(replace)
        quote_list = [k for k in quote_list if k != 'Read complete Powerquote']
        main_list = []
        t = 0
        for h in range(int(len(quote_list)/2)):
            main_list.append((quote_list[h+t], quote_list[h+1+t]))
            t = t+1

        return main_list


def get_quote(category):
    """
    This function take a category as a input and returns
    a random quote which matches the input.
    :param category: Category of quote e.g. Motivational
    :param return:   A tuple (quote, author_of_the_quote)
    """
    quotes = get_quotes(category)
    length = len(quotes)
    if(length == 1):
        quote_with_author_list = []
        quote_with_author_list.append(quotes[0])
        return(tuple(quote_with_author_list))
    else:
        random_number = random.randint(0, length - 1)
        quote_with_author_list = []
        quote_with_author_list.append(quotes[random_number])
        quote_with_author_list.append(person)

        return(tuple(quote_with_author_list))


# quotes = get_quotes("power")
# print(quotes)
# quote = get_quote("motivational")
# print(quote)
