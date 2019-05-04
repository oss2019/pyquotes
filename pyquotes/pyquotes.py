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
	pass

def get_quote(person: (None, str) = None,
			  category: (None, str) = None):
	"""
	This function take a category and a person as a input and returns
	a random quote which matches the input.

	:param person:	 Name of the person e.g. Albert Einstein
	:param category: Category of quote e.g. Motivational
	:param return:   A tuple (quote, author_of_the_quote)
	"""
	pass

def get_quote_of_the_day():
	"""
	This fuction returns quote of the day.

	:param return: A tuple (quote, author_of_the_quote)
	"""
	pass