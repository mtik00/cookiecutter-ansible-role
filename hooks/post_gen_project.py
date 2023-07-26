#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import sys
from pathlib import Path


REMOVE_DIRS = [
    "{% if not cookiecutter.enable_github_actions %}.github/workflows{% endif %}",
]

# Adding .envrc directly to the template makes template development a pain since
# direnv is enabled in the directoy above.  Therefore, create the file dynamically.
DIRENV_ENABLED = "{% if cookiecutter.enable_direnv %}true{% endif %}"
DIRENV = """layout python python3

# Create .secrets/env.sh for exporting repo-specific shell things with sensitive
# data.  .secrets is ignored in .gitignore.
[[ -f .secrets/env.sh ]] && source .secrets/env.sh

# Put repo-specific scripts in a ./bin folder.
PATH_add bin
"""


def remove_dirs(dirs):
    for path in REMOVE_DIRS:
        if path and os.path.exists(path):
            shutil.rmtree(path)


def handle_direnv(enabled: bool = True):
    if enabled:
        Path(".envrc").write_text(DIRENV)


def main():
    remove_dirs(x for x in REMOVE_DIRS if x and os.path.exists(x))
    handle_direnv(DIRENV_ENABLED == "true")

    for path in REMOVE_DIRS:
        if path and os.path.exists(path):
            shutil.rmtree(path)


if __name__ == "__main__":
    main()
