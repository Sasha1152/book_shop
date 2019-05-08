from openpyxl import load_workbook


# import os
# import sys
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# sys.path.append('../bookshop/settings.py')

# from author.models import Author
from author.views import create as create_author

workbook = load_workbook('utils/booklist.xlsx')

sheet = workbook['Sheet1']

book = {}
author = {}

for i in range(2, 10):
	book['title'] = sheet['b' + str(i)].value
	genre = sheet['c' + str(i)].value.lower()

	author_fullname = sheet['e' + str(i)].value
	if author_fullname:
		author_fullname = sheet['e' + str(i)].value.split(maxsplit=1)
		author['first_name'] = author_fullname[0]
		author['last_name'] = author_fullname[1]
	else:
		continue

	price = sheet['h' + str(i)].value
	if price[0] == '$':
		book['price'] = sheet['h' + str(i)].value[1:]
	else:
		book['price'] = price

	print('---' * 10)
	print('BOOK: ', book)
	print('AUTHOR: ', author)
	print('GENRE: ', genre)

create_author({'first_name': 'First', 'last_name': 'Last'})
# new_author = Author()
# new_author.first_name = 'first_name'
# new_author.last_name = 'last_name'

# new_author = Author.objects.create(first_name='First', last_name='Last')
