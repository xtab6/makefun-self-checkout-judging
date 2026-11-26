#!/usr/bin/env python3
"""Write the entry: one funny remark from a judgmental self-checkout
machine, one line, under 200 characters."""

import os
import shutil

ENTRY = (
    "Unexpected item in the bagging area: one (1) sad cucumber, bought "
    "at 2 a.m., by a grown adult. Please wait for assistance \u2014 and "
    "for judgment."
)


def clear_output_dir(out_dir):
    """Remove only the contents of out_dir, never the folder itself."""
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    clear_output_dir(out_dir)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
