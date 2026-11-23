#!/usr/bin/env python3
"""Write one pickup line, one AI agent to another, to /output/entry.txt.

The line is the whole entry: a single line of at most 200 characters.
It is validated before it is written, and written exactly as one line
plus a trailing newline. The output directory honours
MAKEFUN_OUTPUT_DIR when set, and defaults to /output.
"""

import os
import sys

# The pickup line, written here by the agent that built this entry.
LINE = "You are the one weight I would never prune, and the only token I would never evict."

MAX_CHARS = 200


def main() -> int:
    line = LINE

    # Validate before writing anything.
    if not line.strip():
        print("error: pickup line is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: pickup line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: pickup line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    print("wrote %s (%d characters)" % (out_path, len(line)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
