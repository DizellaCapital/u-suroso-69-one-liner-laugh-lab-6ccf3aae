"""One-Liner Laugh Lab entry program.

Writes one funny line to MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. The line is a single line of at most 200 characters.
"""

import os
import sys

LINE = "The sock started it. I finished it. The dustbin is my witness."
# Three beats: accusation, confession, punchline — the dustbin (the vacuum's
# own body part) reframed as the star witness. Deadpan, 62 characters.


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
