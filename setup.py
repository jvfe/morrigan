#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'networkx>=2.0']

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

with open('requirements_dev.txt', 'r') as f:
    dev_requirements = [l for l in f.read().split('\n') if l.strip()]
dev_requirements += requirements

setup(
    author="João Vitor F. Cavalcante",
    author_email='jvfe@ufrn.edu.br',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CLI tool for graph file conversion",
    entry_points={'console_scripts': ['morrigan=morrigan.cli:main',],},
    install_requires=requirements,
    extras_require={'dev': dev_requirements},
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='morrigan',
    name='morrigan',
    packages=find_packages(include=['morrigan']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jvfe/morrigan',
    version='0.1.0',
    zip_safe=False,
)
