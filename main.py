#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt (or $OUTPUT_PATH when set). Deterministic, stdlib only,
no randomness, no network.
"""

import os

TEXT = (
    "WARNING: Contains a human. Handle with care: it will agree to your "
    "face, complain to everyone else, and call this 'being the bigger person.'"
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
