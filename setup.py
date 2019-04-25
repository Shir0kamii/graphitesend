#!/usr/bin/env python

import sys
from setuptools import setup

install_requires = []
if sys.version_info.major == 2:
    install_requires.append('contextlib2')

setup(
    name='graphitesender',
    version='0.11.2',
    description='A simple interface for sending metrics to Graphite',
    author='Alexandre Bonnetain',
    author_email='shir0kamii@gmail.com',
    url='https://github.com/shir0kamii/graphitesender',
    packages=['graphitesend'],
    long_description="https://github.com/shir0kamii/graphitesender",
    entry_points={
        'console_scripts': [
            'graphitesend = graphitesend.graphitesend:cli',
        ],
    },
    install_requires=install_requires,
    extras_require={
        'asynchronous': ['gevent>=1.0.0'],
        'cli': ['argparse'],
    }
)
