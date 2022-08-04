#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import sys
from pathlib import Path


REMOVE_DIRS = [
    '{% if cookiecutter.enable_github_actions != "yes" %}.github/workflows{% endif %}',
]

# Adding .envrc directly to the template makes template development a pain since
# direnv is enabled in the directoy above.  Therefore, create the file dynamically.
DIRENV_ENABLED = '{% if cookiecutter.enable_direnv == "yes" %}true{% endif %}'
DIRENV = """layout python python3

[[ -f .secrets/env.sh ]] && source .secrets/env.sh

PATH_add bin
"""

def main():
    for path in REMOVE_DIRS:
        if path and os.path.exists(path):
            shutil.rmtree(path)

    if DIRENV_ENABLED == "true":
        Path(".envrc").write_text(DIRENV)


if __name__ == "__main__":
    main()
