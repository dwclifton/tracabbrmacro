#!/usr/bin/env python

import os.path
from setuptools import setup

setup(
    name = 'TracAbbrMacro',
    packages = ['abbr'],
    version = '0.11.0',

    author = 'Douglas Clifton',
    author_email = 'dwclifton@gmail.com',
    description = 'Return an abbr|acronym element with title attribute.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    keywords = '0.11 abbr dwclifton macro wiki',
    url = 'http://trac-hacks.org/wiki/AbbrMacro',
    license = 'BSD',

    entry_points = { 'trac.plugins': [ 'abbr.macro = abbr.macro' ] },
    classifiers = ['Framework :: Trac'],
    install_requires = ['Trac'],
)
