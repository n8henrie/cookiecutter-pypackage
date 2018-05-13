import re
from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as readme_file,\
        open('CHANGELOG.md', encoding='utf-8') as history_file:
    readme = readme_file.read()
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = [
            line for line in requirements_file.read().splitlines()
            if not line.startswith('-i ')
            ]

with open('requirements-dev.txt') as dev_requirements_file:
    dev_requirements = [
            line for line in dev_requirements_file.read().splitlines()
            if not line.startswith('-i ')
            ]

with open('requirements-test.txt') as test_requirements_file:
    test_requirements = test_requirements_file.read().splitlines()
    dev_requirements.extend(test_requirements)

version_regex = re.compile(r'__version__ = [\'\"]v((\d+\.?)+)[\'\"]')
with open('src/{{ cookiecutter.repo_name }}/__init__.py') as f:
    vlines = f.readlines()
__version__ = next(re.match(version_regex, line).group(1) for line in vlines
                   if re.match(version_regex, line))

setup(
    name="{{ cookiecutter.repo_name }}",
    version=__version__,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + "\n\n" + history,
    long_description_content_type='text/markdown',
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    packages=find_packages("src"),
    include_package_data=True,
    package_dir={"": "src"},
    # entry_points={
    #     'console_scripts': ['{{ cookiecutter.repo_name }}={{ cookiecutter.repo_name }}.cli:run']
    #     },
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords="{{ cookiecutter.repo_name }}",
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6"
    ],
    extras_require={
        "dev": dev_requirements
        },
    test_suite="tests",
    tests_require=test_requirements,
    python_requires=">=3.6",
)
