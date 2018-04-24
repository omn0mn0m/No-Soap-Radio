#!/usr/bin/env python

from distutils.core import setup

setup(
    name='No-Soap-Radio',
    version='0.1',
    description='Software-Defined Radio (SDR) transceiver software meant to be run on a Raspberry Pi',
    author='Nam Tran',
    author_email='tranngocnam97@gmail.com',
    url='https://omn0mn0m.github.io/No-Soap-Radio/',
    tests_require=['pytest'],
    install_requires=[],
    packages=['no_soap_radio'],
    include_package_data= True,
    platforms='any',
    test_suite='no_soap_radio.test.test_no_soap_radio',
    extras_require={
        'testing': ['pytest'],
    },
)
