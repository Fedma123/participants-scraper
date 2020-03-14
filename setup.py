from setuptools import setup

setup(
   name='participants-scraper',
   version='1.0',
   description='Module for scraping Google Meet Participants',
   packages=['participants-scraper'],  #same as name
   install_requires=['beautifulsoup4'], #external packages as dependencies
)
