# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='ci-jenkins-tox-example',
    version='1.0',
    packages=['example'],
    author='Sebastian Buczyński',
    author_email='poczta@enforcer.pl',
    install_requires=[
        'nose==1.3.4',
        'behave==1.2.5'
    ]
)
