import urllib

#Read text from document
def read_text():
	quotes = open("/Users/eliasvensson/Udacity/full-stack/PFWP/check_profanity/movie_quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
read_text()