#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='prodactivity',
    version='0.1.dev0',
    author='Za Wilgustus',
    author_email='za@f5.com',
    license='Apache 2.0',
    url='https://github.com/F5Networks/f5-container-utils.git',
    packages=find_packages(),
    scripts=['cli/develop'],
    install_requires=[
            'jinja2 >= 2.8, < 3'
        ]
)
