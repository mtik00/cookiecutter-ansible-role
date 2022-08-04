#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import sys

REMOVE_DIRS = [
    '{% if cookiecutter.enable_github_actions != "yes" %}.github/workflows{% endif %}',
]


def main():
    for path in REMOVE_DIRS:
        if path and os.path.exists(path):
            shutil.rmtree(path)


if __name__ == "__main__":
    main()
