#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed, to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to
/output). Python 3 standard library only; no input, no network, no
randomness, so the output is byte-identical on every run.
"""

import os

# One line, well under the 160-character cap. The joke is specific and
# changelog-shaped: the fix is not "sleep works now" but the exact
# bedtime bug it removes, and the payoff stays in release-note voice.
ENTRY = (
    "Fixed: humans no longer lie awake replaying every embarrassing "
    "thing they have said since 2009; sleep now starts on time."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
