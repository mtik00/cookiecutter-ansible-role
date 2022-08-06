# Developing this role

## Initial configuration

Run this script for initial setup (just after `cookiecutter`):
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

## Ongoing development

1. Use a Python virtual environment
2. Make sure pre-commit and commitizen are installed (`pip install -r requirements.txt)
3. Make sure pre-commit hooks are installed:  
    pre-commit autoupdate
    pre-commit install
    pre-commit install --hook-type commit-msg
4. Use `commitizen`-styled commit messages
5. Use `cz bump` to control versioning
