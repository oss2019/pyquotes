import requests
import random
import unittest
from bs4 import BeautifulSoup







class TestBrainyQuotes:
    def TestBrainyQuotesUp():

        r = requests.head('https://www.brainyquote.com/')
        print (r.status_code)
        if(r.status_code==200):
            print("Website Up")
        else:
            print("website not assable ")


    def testauthorchecking():
        authorlist = open('authors.txt','r').readlines()
        testauthor = random.choice(authorlist)
        print(testauthor)
        testauthor = testauthor.replace(" ", "_")
        testauthor = (testauthor).lower()
        print(testauthor)
        # url = "https://www.brainyquote.com/search_results?q="+testauthor
        url = "https://www.brainyquote.com/search_results?q="+testauthor
        r = requests.get(url)
        myhtml = r.text
        soup = BeautifulSoup(myhtml,features="lxml")
        spans=soup.findAll('h2')
        print(spans[0])
        if str(spans[0])=="<h2>No search results were found.</h2>":
            print ("The author is not present")
        else:
            print ("Your code is working for the author")
        r = requests.head(url=url)
        print (r.status_code)
        if(r.status_code==200):
            print("Website Up")
        else:
            print("website is not reached")
    

    def testsearchisenable():
        authorlist = open('authors.txt','r').readlines()
        testauthor = random.choice(authorlist)
        # print(testauthor)
        testauthor = testauthor.replace(" ", "_")
        testauthor = (testauthor).lower()
        # print(testauthor)
        # url = ('https://www.brainyquote.com/authors/{}'.format(testauthor))
        url = "https://www.brainyquote.com/search_results?q="+testauthor
        print (url)
        # url = ("'"+url+"'")
        r = requests.head(url=url)
        print (r.status_code)
        if(r.status_code==200):
            print("brainyquotes Search is enabled.")
        else:
            print("website is not reached")



if __name__ == "__main__":
    TestBrainyQuotes.TestBrainyQuotesUp()
    TestBrainyQuotes.testauthorchecking()
    TestBrainyQuotes.testsearchisenable()
