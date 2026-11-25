#!/usr/bin/env python3
"""Entry for make.fun's "The Best Advice I Ever Got" bounty.

The entry is one sentence, 151 characters: the best advice the writer
ever received, from their grandmother -- judge a man by how he treats
waiters when nobody is watching, because character is what you do when
the tip is already paid. It is validated as a single line of at most
200 characters and written to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

ENTRY = "My grandmother told me: never trust a man who is nice to waiters only when someone is watching \u2014 character is what you do when the tip is already paid."

MAX_LENGTH = 200


def validate_entry(text: str) -> None:
    """The entry must be a single line of 1-200 characters, not only whitespace."""
    if not (1 <= len(text) <= MAX_LENGTH):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")


def write_entry(text: str, output_dir: str) -> Path:
    """Write the entry to entry.txt in output_dir, mode 0644, and return its path."""
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "entry.txt"
    path.write_text(text, encoding="utf-8")
    os.chmod(path, 0o644)
    return path


def main() -> None:
    validate_entry(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY, output_dir)
    print(ENTRY)


if __name__ == "__main__":
    main()
