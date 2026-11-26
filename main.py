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


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the contents of /output; never remove the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
