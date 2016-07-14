# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='raspyedge',
    version='0.0.1',
    description='An application to connect a raspberry pi to AWS IoT',
    long_description=readme,
    author='Alexander Schmitt',
    author_email='alexander.schmitt@web.de',
    url='https://github.com/ac-schmitt/raspyedge',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

