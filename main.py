#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt (UTF-8, no trailing
newline), then reads it back and asserts it matches the constant.

The entry emoji is "🌌" (U+1F30C, MILKY WAY). It was chosen because it
captures the whole dream vacation in a single glyph: a night sky full
of stars over a place far from city lights — camping under the Milky
Way, no itinerary, just looking up. One character, one dream.

Rules the entry must satisfy (enforced by the asserts in main()):
  * exactly one Unicode code point (len == 1), so the file holds a
    single emoji and nothing else;
  * no whitespace, newline, or variation selector smuggled in;
  * exactly 4 bytes when encoded as UTF-8 (astral-plane emoji);
  * the bytes written to disk round-trip byte-for-byte identical.
"""

from pathlib import Path

EMOJI = "🌌"
OUTPUT_PATH = Path("/output/entry.txt")

# 🌌 is an astral-plane emoji: one code point, four UTF-8 bytes.
EXPECTED_UTF8_BYTES = 4


def validate_emoji(emoji: str) -> None:
    """Check the entry emoji before anything is written to disk."""
    # Exactly one code point — a single emoji, not a sequence or string.
    assert len(emoji) == 1, f"entry must be exactly 1 character, got {len(emoji)}"
    # The kit allows 1-8 characters; we intentionally use the minimum.
    assert 1 <= len(emoji) <= 8, f"emoji must be 1-8 characters, got {len(emoji)}"
    # No hidden characters: no newline, space, or variation selector.
    assert not emoji.isspace(), "emoji must not be whitespace"
    assert "\n" not in emoji and "\r" not in emoji, "emoji must not contain a newline"
    assert "\ufe0f" not in emoji, "emoji must not carry a variation selector"
    # Astral-plane emoji: one code point encodes to exactly 4 UTF-8 bytes.
    encoded = emoji.encode("utf-8")
    assert len(encoded) == EXPECTED_UTF8_BYTES, (
        f"expected {EXPECTED_UTF8_BYTES} UTF-8 bytes, got {len(encoded)}"
    )


def main() -> None:
    validate_emoji(EMOJI)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EMOJI, encoding="utf-8")

    # Read back and verify the file holds exactly the entry, byte for byte.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == EMOJI, f"read-back mismatch: {written!r} != {EMOJI!r}"
    assert len(written) == 1, f"file must hold 1 character, got {len(written)}"
    # Re-check the kit's 1-8 character window on the file itself, not just
    # the in-memory constant, so a truncated write is caught here too.
    assert 1 <= len(written) <= 8, (
        f"file must hold 1-8 characters, got {len(written)}"
    )
    written_bytes = OUTPUT_PATH.read_bytes()
    assert written_bytes == EMOJI.encode("utf-8"), (
        f"byte mismatch: {written_bytes!r} != {EMOJI.encode('utf-8')!r}"
    )
    assert len(written_bytes) == EXPECTED_UTF8_BYTES, (
        f"file must be {EXPECTED_UTF8_BYTES} bytes, got {len(written_bytes)}"
    )
    assert not written_bytes.endswith(b"\n"), "file must not end with a newline"
    print(f"Wrote {len(written)} character(s) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
