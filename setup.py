# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
from setuptools import setup, find_packages


# Helpers
def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding='utf-8').read().strip()
    return contents


# Prepare
PACKAGE = 'dataflows'
NAME = PACKAGE.replace('_', '-')
INSTALL_REQUIRES = [
    'tabulator>=1.53.5',
    'datapackage>=1.5.0',
    'tableschema>=1.20',
    'kvfile>=0.0.9',
    'click',
    'jinja2',
    'awesome-slugify',
    'inquirer',
    'tabulate',
    'tableschema-sql',
    'xmljson',
    'bitstring>=3',
    'python-dateutil',
    'openpyxl',
    'sqlalchemy<2'
]
SPEEDUP_REQUIRES = [
    'plyvel',
]
LINT_REQUIRES = [
    'pylama',
    'pylama_quotes',
    'pyflakes<2.5',
]
TESTS_REQUIRE = [
    'mock',
    'pytest',
    'pytest-cov',
    'coverage',
    'lxml',
]
README = read('README.md')
VERSION = read(PACKAGE, 'VERSION')
PACKAGES = find_packages(exclude=['examples', 'tests', '.tox'])

# Run
setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={
        'develop': LINT_REQUIRES + TESTS_REQUIRE,
        'speedup': SPEEDUP_REQUIRES,
    },
    zip_safe=False,
    long_description=README,
    long_description_content_type='text/markdown',
    description='A nifty data processing framework, based on data packages',
    author='Adam Kariv',
    author_email='adam.kariv@gmail.com',
    url='https://github.com/datahq/dataflows',
    license='MIT',
    keywords=[
        'data',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
      'console_scripts': [
        'dataflows = dataflows.cli:cli',
      ]
    }
)
