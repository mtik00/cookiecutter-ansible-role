# cookiecutter-ansible-role

This is a cookiecutter template for creating an ansible role for `git` usage.

## Usage
You can reference this GitHub repository directory by running:
```
cookiecutter gh:mtik00/cookiecutter-ansible-role
```

A new folder will be created in `$CWD`.

## Role Development
After creating the role from the cookiecutter template, set up your environment
for development.

The template assumes you are using Python as your dev environment and installs both [pre-commit(https://pre-commit.com/) and [commitizen](https://commitizen-tools.github.io/commitizen/).

The following assumes you already have a virtual environment activated (or you are using `direnv`).
```
git init .
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pre-commit autoupdate
pre-commit install
pre-commit install --hook-type commit-msg
git add .
git commit -m"feat: initial checkin"
cz changelog
git add CHANGELOG.md
git commit -m"docs: adding changelog"
cz bump
```
