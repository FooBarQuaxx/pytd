#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for pytd.
"""

import setuptools

from pytd import __project__, __version__

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder, readme is generated on release
#CHANGES = open('CHANGES.rst').read()

setuptools.setup(
    name=__project__,
    version=__version__,

    description="A flasky application for terminologies search and translation.",
    url='https://github.com/abessifi/pytd',
    author='Ahmed Bessifi',
    author_email='ahmed.bessifi@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    #long_description=(README + '\n' + CHANGES),
    long_description=(README),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: GNU/Linux',
        'Programming Language :: Python :: 2.7',
    ],

    #install_requires=open('requirements.txt').readlines(),
)
