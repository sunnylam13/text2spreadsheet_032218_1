try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'This program reads several text files and sticks the content into a spreadsheet, one line per row.  Each text file gets a column of its own.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/text2spreadsheet_032218_1',
	'download_url': 'https://github.com/sunnylam13/text2spreadsheet_032218_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['openpyxl, sys, os, re'],
	'scripts': [],
	'name': 'Text Files to Spreadsheet'
}

setup(**config)