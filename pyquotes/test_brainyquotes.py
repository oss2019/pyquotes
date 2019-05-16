import unittest
import brainyquote

class SimpleTest(unittest.TestCase):

    def test_quote_of_the_day(self):
        # Test case for quote of the day
        quote_of_the_day = brainyquote.get_quote_of_the_day()
        self.assertTrue(quote_of_the_day, "No quote generated")
        length = len(quote_of_the_day)
        self.assertEqual(length, 2, "Invalid return format")
        quote = quote_of_the_day[0].replace(' ', '')
        self.assertNotEqual(quote, "", "Quote is Empty")
        author = quote_of_the_day[1].replace(' ', '')
        self.assertNotEqual(author, "", "Author Name is Empty")

    def test_no_data(self):
        # Test case for input which would give no valid output
        error_message = '''Oops! It seems that there are no quotes of the author of that category. \nYou may consider changing the category or the author '''
        quote_list = brainyquote.get_quote("abc", "def")
        self.assertEqual(quote_list, error_message)
        quote_list = brainyquote.get_quotes("abc", "def")
        self.assertEqual(quote_list, error_message)

    def test_for_quote(self):
        # Test for checking if mock data is present in the list of quotes
        quote = ["Everything has beauty, but not everyone sees it.", "confucius"]
        quote_list = brainyquote.get_quotes("confucius", "beauty")
        self.assertIn(quote, quote_list, "Wrong quotes are being generated")

    def test_for_single_quote(self):
        # Test for checking single quote is from list of all quotes
        quote_list = brainyquote.get_quotes("confucius", "brainy")
        quote = brainyquote.get_quote("confucius", "brainy")
        self.assertIn(quote[0], quote_list, "Wrong quotes are being generated")

    def test_for_author(self):
        # Test for checking quote is of correct author
        author = "confucius"
        quote = brainyquote.get_quote(author, "long")
        self.assertEqual(quote[0][1], author, "Wrong author's quote")

    def test_for_case_sensitiveness(self):
        # Test for checking if input is not case sensitive
        quote_list1 = brainyquote.get_quotes("confucius", "motivational")
        quote_list2 = brainyquote.get_quotes("Confucius", "Motivational")
        quote_list3 = brainyquote.get_quotes("confucius", "MotiVatIonal")
        quote_list4 = brainyquote.get_quotes("CoNfuCius", "motivational")
        quote_list5 = brainyquote.get_quotes("conFUCiuS", "moTIvaTIonal")
        self.assertEqual(quote_list1, quote_list2, "Input is case sensitive")
        self.assertEqual(quote_list1, quote_list3, "Input is case sensitive")
        self.assertEqual(quote_list1, quote_list4, "Input is case sensitive")
        self.assertEqual(quote_list1, quote_list5, "Input is case sensitive")

if __name__ == '__main__':
    unittest.main()
