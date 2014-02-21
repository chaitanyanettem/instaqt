import re
import lxml
import time
import psycopg2

remove_links = re.compile('[A-Za-z0-9')

class page:
	raw = []
	categories = []
	page_title = ""
	def __init__(self,raw,page_title):
		self.raw = raw.split('\n')
		self.page_title = page_title
		#To-Do: Save other relevant data.

	def remove_italics_bold(self):
		more_quotes = True
		for line in self.raw:
			if line.startswith('*') && more_quotes is True:
				line.replace("''","")
				line.replace("'''","")
				print line
				#To-Do: Store in database with psycopg2
			elif line.startswith('== See Also') or line.startswith('==See Also=='):
				more_quotes = False
				continue
			elif line.startswith("[[Category:"):
				#To-Do: Save categories

if __name__ == "__main__":
	quotedb = open("enwikiquote-20140121-pages-articles.xml")
	quotedb = quotedb.read() #Will load entire xml dump into memory. Make sure enough RAM is available.

	##To-Do: Code to parse xml with lxml. Parsing must be done page by page
	##To-Do: Check if redirect tag exists for each page. If it does then store an indication of the same in DB.
	##To-Do: 
