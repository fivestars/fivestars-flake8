#! /usr/bin/env python
from setuptools import setup

setup(
    name='fivestars-flake8',
    version='1.0.0',
    description='flake8 extensions for FiveStars',
    long_description='flake8 extensions for FiveStars [mutabledefaults]',
    keywords='flake8 fivestars mutabledefaults',
    author='FiveStars',
    auther_email='dev@fivestars.com',
    url='https://github.com/fivestars/fivestars-flake8',
    license='MIT',
    py_modules=['fivestars_flake8'],
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'flake8.extension': [
            # 'FS00 = fivestars_flake8:TestIt',
            'FS01 = fivestars_flake8:MutableDefaultArgumentValues',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
