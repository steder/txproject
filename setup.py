#!/usr/bin/env python

from distutils.core import setup

setup(name='txProject',
      version='1.0.0a1',
      description='Twisted Project Skeleton Creator',
      author='Mike Steder',
      author_email='steder@gmail.com',
      url='http://bitbucket.org/steder/txproject',
      packages=['txproject',],
      scripts=['bin/dirprinter', 'bin/txproject']
     )
