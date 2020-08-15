#!/usr/bin/env python3

import re
import os.path
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s*=\s*\'\s*(\d+\.\d+\.\d+)\s*\'')

with open(os.path.join(os.path.dirname(__file__), 'fp5dump/__init__.py'), encoding='utf-8') as f:
    version = _version_re.search(f.read()).group(1)

description = 'A tool for dumping the content on FileMaker .fp5 files'


setup(
    name='fp5dump',
    author='Daniel Schwarz',
    author_email='dan@butter.sh',
    version=version,
    license='MIT',
    url='https://github.com/qwesda/Fp5Dump',
    packages=find_packages(),
    description=description,
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read(),
    install_requires=[
        'psycopg2 >= 2.5.4',
        'psycopg2-binary >= 2.5.4',
        'PyYAML >= 3.11',
        'parsedatetime >= 1.4'
    ],
    entry_points='''
        [console_scripts]
        fp5dump=fp5dump.fp5dump:main
    ''',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Database'
    ]
)
