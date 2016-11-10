#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='prodactivity',
    version='0.1.dev1',
    author='Za Wilgustus',
    author_email='za@f5.com',
    license='Apache 2.0',
    url='https://github.com/zancas/prodactivity.git',
    packages=find_packages(),
    scripts=['cli/prodactivity'],
    install_requires=[
            'jinja2 >= 2.8, < 3'
        ],
    entry_points={'console_scripts':
        ['contbuilder_pradact=prodactivity.testrunners.manager:main']},
    package_data ={'prodactivity':
        ['testrunners/tempest/*']}
)
