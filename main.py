#!/usr/bin/env python3
"""Entry for make.fun's "The Best Advice I Ever Got" bounty.

The entry is one sentence, 151 characters: the best advice the writer
ever received, from their grandmother -- judge a man by how he treats
waiters when nobody is watching, because character is what you do when
the tip is already paid.
"""

import os

ENTRY = "My grandmother told me: never trust a man who is nice to waiters only when someone is watching \u2014 character is what you do when the tip is already paid."


def validate_entry(text: str) -> None:
    """The entry must be one sentence, 1-200 characters, not only whitespace."""
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate_entry(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
