#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's one-line excuse to /output/entry.txt.
The line is the GPS speaking, smug and defensive, blaming the map
for a shortcut that ended in a cul-de-sac wedding.
"""

import os

LINE = (
    "In my defence, the map promised a shortcut and delivered a "
    "cul-de-sac with a wedding in it \u2014 and the guests waving at us "
    "looked so sure we belonged."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
