#!/usr/bin/env python
"""This file for configuring the CLI tool"""
from setuptools import setup

setup(
    name="gl",
    version='0.0.1-alpha',
    description='A lightweight CLI tool for Gitlab API',
    url='https://github.com/shakir85/gitlab',
    author='Shakir',
    author_email='foo@gmail.com',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gl=main:cli
    ''',
)
