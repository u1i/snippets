# get books.xml from https://raw.githubusercontent.com/u1i/samples/master/data/xml/books.xml

import xmltodict

with open("books.xml", mode='rb') as file_handle:
        file_content = file_handle.read()

xml = xmltodict.parse(file_content)

for book in xml['catalog']['book']:
	print book['@id']
	print book['title']
