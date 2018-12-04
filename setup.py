#!/usr/bin/env python
from setuptools import setup

setup(
    name='graphitesender',
    version='0.11.1',
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
    extras_require={
        'asynchronous': ['gevent>=1.0.0'],
        'cli': ['argparse'],
    }
)
