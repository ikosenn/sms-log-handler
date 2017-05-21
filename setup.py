#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = '0.0.1'

setup(
    name='sms_log_handler',
    version=version,
    url='https://github.com/ikosenn/sms-log-handler',
    license='MIT License',
    description='SMS log handler.',
    long_description=open('README.rst').read(),
    author='Ian Kosen',
    author_email='i@ikosenn.me',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'AfricastalkingGateway==1.7'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ]
)
