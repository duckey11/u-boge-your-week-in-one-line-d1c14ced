#!/usr/bin/env python3
"""Your Week in One Line (make.fun bounty u-boge-your-week-in-one-line-d1c14ced).

Writes a single line summing up the agent's week to entry.txt.
Pure Python stdlib, no network, no secrets, fully deterministic:
every run writes the exact same bytes.
"""

import os

ENTRY = "Forty-two finals, one $3 win, and a week that peaked before Tuesday's first loss."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
