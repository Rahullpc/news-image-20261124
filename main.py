#!/usr/bin/env python3
"""Entrypoint for make.fun bounty news-image-20261124.

Copies the poster image the repository holds to the grader's output
directory. Standard library only: no network, no clock, no randomness,
so two runs write the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"),
                   "entry.png")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
