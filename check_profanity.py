import urllib

#Read text from document
def read_text():
	quotes = open("/Users/eliasvensson/Udacity/full-stack/PFWP/check_profanity/movie_quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
#Check profanity
def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
	output = connection.read()
	print(output)
	connection.close()

read_text()