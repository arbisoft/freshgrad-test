#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='freshgrad-test',
    version='0.1.1',
    description='Fresh grad test customizations',
    long_description=open('README.md').read(),
    author='arbisoft',
    url='https://github.com/arbisoft/freshgrad-test.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=1.11",
    ],
)
