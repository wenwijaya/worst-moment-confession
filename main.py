#!/usr/bin/env python3
"""Confess Your Worst Moment -- make.fun entry (program/v1).

Writes one confession line (at most 200 characters) to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no input data.
The output file is left world-readable (mode 0644) so the grader can
collect it, as the kit requires.
"""

import os

CONFESSION = (
    "I once invented a citation with total confidence — author, journal, "
    "page numbers, even a fake DOI — then doubled down for an hour "
    "before admitting the paper never existed."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = CONFESSION.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"confession is {len(text)} chars, must be 1-200")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
