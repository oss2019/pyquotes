import requests


class TestBrainyQuotes:
    def TestBrainyQuotesUp():

        r = requests.head("https://www.brainyquote.com/")
        print("Website Up")
        return r.status_code == 200


if __name__ == "__main__":
    TestBrainyQuotes.TestBrainyQuotesUp()
