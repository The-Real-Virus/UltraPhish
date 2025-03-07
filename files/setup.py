#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='UltraPhish',
    version=version,
    description='Ultimate phishing tool in python with dual tunneling, 77 templates and many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='The-Real-Virus',
    author_email='societycyber9@gmail.com',
    license="MIT",
    url='https://github.com/The-Real-Virus/UltraPhish',
    scripts=['ultraphish'],
    install_requires=["requests", "rich"]
)
