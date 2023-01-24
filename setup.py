from setuptools import setup
from django4_rest_swagger import __version__ as VERSION

README = """
Django4 REST Swagger

An API documentation generator for Django 4, Swagger UI and Django REST Framework.

Installation
From pip:

pip install django4-rest-swagger
"""

setup(
	name='django4-rest-fswagger',
	version=VERSION,
	install_requires=[
		'Django>=4.1.5',
		'djangorestframework>=3.14.0',
		'coreapi>=2.3.3',
		'openapi-codec>=1.3.2',
		'simplejson',
	],
	packages=['django4-rest-swagger'],
	include_package_data=True,
    license='FreeBSD License',
    description='Swagger UI for Django 4 & Django REST Framework 3+',
    long_description=README,
    author='Jorge Salgado',
    author_email='contacto@jorgesalgado.com.mx',
	url='https://github.com/JorgeSalgado7/django4-rest-swagger'
)