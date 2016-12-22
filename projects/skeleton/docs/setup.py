try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'BMI Project',
	'author' : 'Shel Benfield',
	'url' : 'URL to get it at.',
	'download_url' : 'Where to download it.',
	'author_email' : 'shelbenfield@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages': ['NAME'],
	'scripts' : [],
	'name' : 'projectname'
}

setup(**config)