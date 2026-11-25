#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's one-line excuse to /output/entry.txt.
The line is the GPS speaking, mid-recalculation, smug and defensive,
blaming the map for a shortcut that ended in a cul-de-sac wedding —
and brazening it out as if the wedding guests expected us.
"""

import os

LINE = (
    "Recalculating: the map promised a shortcut and delivered a "
    "cul-de-sac with a wedding in it \u2014 and the guests are waving "
    "like we belong here."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
