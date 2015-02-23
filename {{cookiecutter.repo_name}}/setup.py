#! /usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import pypandoc

def md_to_rst(infile):
    return pypandoc.convert(infile, 'rst')

readme = md_to_rst('README.md')
history = md_to_rst('HISTORY.md')

requirements = [
        # TODO: Add any additional requirements for all templates
]

test_requirements = [
    'pytest>=2.6.4'
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme + '\n\n' + history,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    package_dir={'{{ cookiecutter.repo_name }}':
                 '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
