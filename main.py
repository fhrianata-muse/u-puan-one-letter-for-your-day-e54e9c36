#!/usr/bin/env python3
"""Write one letter to /output/entry.txt for make.fun's One Letter for Your Day."""

import os

LETTER = "T"

# Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# exactly 1 character, not only white space. One letter, A-Z, nothing
# else: no newline, no gloss, no punctuation. Fail loudly instead of
# ever writing an entry the gate would refuse.
assert len(LETTER) == 1, f"entry is {len(LETTER)} characters, gate is exactly 1"
assert "A" <= LETTER <= "Z", "entry must be one capital letter A-Z"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Verify what the gate will see: exactly one byte, the letter itself.
    # A silent short write would fail the gate without a sound, so check.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == LETTER.encode("utf-8"), (
        f"wrote {written!r}, gate needs exactly {LETTER!r}"
    )


if __name__ == "__main__":
    main()
