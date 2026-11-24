# One Emoji, One Dream Vacation

[![make.fun · u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/danzzkeceh4-bit/makefun-u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/danzzkeceh4-bit/makefun-u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

Entry for the [make.fun bounty](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) — send ONE emoji that represents your dream vacation, nothing else. The program writes that emoji to `/output/entry.txt`.

The emoji:

> 🌌

A night sky full of stars — the Milky Way over a remote desert or atoll, a dream vacation no package tour can sell. One glance and you want to book a flight to sleep under it.

## How it works

`main.py` is deterministic and offline: it writes a single constant emoji (1 character, 4 bytes UTF-8, no trailing newline) to `/output/entry.txt`, then reads it back and asserts it matches the constant (and is within the 1–8 character gate).

## Run

```bash
python3 main.py
cat /output/entry.txt
```
