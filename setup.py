#! /usr/bin/env python

from setuptools import setup, find_packages
import prodactivity

setup(
    name='prodactivity',
    version=prodactivity.__version__,
    author='Za Wilgustus',
    author_email='za@f5.com',
    license='Apache 2.0',
    url='https://github.com/zancas/prodactivity.git',
    packages=find_packages(),
    scripts=['cli/prodactivity'],
    install_requires=[
            'jinja2 >= 2.8, < 3'
        ],
    entry_points={'console_scripts': [
        'publish_test_container=prodactivity.testrunners.manager:main']},
    package_data={'prodactivity': [
        'testrunners/tempest/Dockerfile',
        'testrunners/tempest/set_tempest_config.sh',
        'testrunners/tempest/project_docker.tmpl',
        'environments/user/*',
        'environments/base/*',
        'testrunners/tempest/config-files/accounts.yaml',
        'testrunners/tempest/config-files/tempest.conf']}
)
