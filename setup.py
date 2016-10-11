#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Neo4j.
# https://github.com/josl/neo4j-02807

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from setuptools import setup, find_packages
from Neo4j import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='Neo4j',
    version=__version__,
    description='Graph databases-02807',
    long_description='''
Graph databases-02807
''',
    keywords='ne4j graph databases',
    author='Jose L. Bellod Cisneros',
    author_email='bellod.cisneros@gmail.com',
    url='https://github.com/josl/neo4j_02807',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'neo4j-driver'
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you
        # get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'Neo4j=Neo4j.cli:main',
        ],
    },
)
