#!/usr/bin/env python3
"""Write the competition entry to MAKEFUN_OUTPUT_DIR (or /output)."""
import os
import sys

TEXT = "🧸\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir!r}: {exc}", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
