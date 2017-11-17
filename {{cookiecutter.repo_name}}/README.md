# {{ cookiecutter.project_name }}

master: [![master branch build status](https://travis-ci.org/n8henrie/{{ cookiecutter.repo_name }}.svg?branch=master)](https://travis-ci.org/n8henrie/{{ cookiecutter.repo_name }}/branches)
<!-- dev: [![dev branch build status](https://travis-ci.org/n8henrie/{{ cookiecutter.repo_name }}.svg?branch=dev)](https://travis-ci.org/n8henrie/{{ cookiecutter.repo_name }}/branches) -->

{{ cookiecutter.project_short_description }}

- Free software: MIT
- Documentation: https://{{ cookiecutter.repo_name }}.readthedocs.io

## Features

- TODO

## Introduction

- TODO

## Dependencies

- Python >= 3.6
- See `requirements.txt`

## Quickstart

1. `pip3 install {{ cookiecutter.repo_name }}`
- TODO

### Development Setup

1. Clone the repo: `git clone https://github.com/n8henrie/{{ cookiecutter.repo_name }} && cd
   {{ cookiecutter.repo_name }}`
1. Make a virtualenv: `python3 -m venv venv`
- TODO

## Configuration

- TODO

## Acknowledgements

- TODO

## Troubleshooting / FAQ

- How can I install an older / specific version of {{ cookiecutter.project_name }}?
    - Install from a tag:
        - pip install git+git://github.com/n8henrie/{{ cookiecutter.repo_name }}.git@v0.1.0
    - Install from a specific commit:
        - pip install git+git://github.com/n8henrie/{{ cookiecutter.repo_name }}.git@aabc123def456ghi789
