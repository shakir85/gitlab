#!/usr/bin/env python
from setuptools import setup

setup(
    name="gl",
    version='0.1',
    description='Will be updated',
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
