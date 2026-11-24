#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt (UTF-8, no trailing
newline), then reads it back and asserts it matches the constant.
"""

from pathlib import Path

EMOJI = "🌌"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(EMOJI) <= 8, f"emoji must be 1-8 characters, got {len(EMOJI)}"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EMOJI, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == EMOJI, f"read-back mismatch: {written!r} != {EMOJI!r}"
    assert 1 <= len(written) <= 8
    print(f"Wrote {len(written)} character(s) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
