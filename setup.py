'''
Created on Oct 4, 2017

@author: peperk
'''
from setuptools import setup

setup(name='py-rest-api',
      version='1.0',
      description='REST on openshift',
      author='peperk',
      author_email='peperk AT gmail',
      include_package_data=True,
      url='',
      install_requires=[
        'scrapy>=1.4.0',
        'Flask>=0.12.2', 
        'MarkupSafe',
        'lxml', 
        'requests', 
        'apscheduler', 
        'unidecode' 
      ],
)