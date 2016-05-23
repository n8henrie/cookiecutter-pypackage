# -*- coding: utf-8 -*-

import re
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
    history = pypandoc.convert('HISTORY.md', 'rst')
except ImportError:
    with open('README.md') as readme_file, open('HISTORY.md') as history_file:
        readme = readme_file.read()
        history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('requirements-dev.txt') as dev_requirements_file:
    dev_requirements = dev_requirements_file.read().splitlines()

version_regex = re.compile(r'__version__ = [\'\"]((\d+\.?)+)[\'\"]')
with open('src/{{ cookiecutter.repo_name }}/__init__.py') as f:
    vlines = f.readlines()
__version__ = next(re.match(version_regex, line).group(1) for line in vlines
                   if re.match(version_regex, line))

setup(
    name="{{ cookiecutter.repo_name }}",
    version=__version__,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + "\n\n" + history,
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    packages=find_packages('src'),
    package_dir={"": "src"},
    include_package_data=True,
    # entry_points={
    #     'console_scripts': ['{{ cookiecutter.repo_name }}={{ cookicutter.repo_name }}.cli:run']
    #     },
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords="{{ cookiecutter.repo_name }}",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
    ],
    extras_require={
        "dev": dev_requirements
        },
    test_suite="tests",
    tests_require=['pytest>=2.8.7']
)
