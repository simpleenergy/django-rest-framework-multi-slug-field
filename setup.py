#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import rest_framework_msf

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = rest_framework_msf.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-rest-framework-multi-slug-field',
    version=version,
    description="""A field for representing a relationship via multiple fields on the target""",
    long_description=readme + '\n\n' + history,
    author='Piper Merriam',
    author_email='piper@simpleenergy.com',
    url='https://github.com/simpleenergy/django-rest-framework-multi-slug-field',
    packages=[
        'rest_framework_msf',
    ],
    include_package_data=True,
    install_requires=[
        'djangorestframework>=2.3.14'
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-rest-framework-multi-slug-field',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
