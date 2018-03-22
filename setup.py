try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'This program reads several text files and sticks the content into a spreadsheet, one line per row.  Each text file gets a column of its own.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'My email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['openpyxl'],
	'scripts': [],
	'name': 'Text Files to Spreadsheet'
}

setup(**config)