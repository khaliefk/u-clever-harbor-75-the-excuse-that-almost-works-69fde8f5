"""Write the one-line excuse to the output file.

The grader mounts a fresh output directory at /output and sets
MAKEFUN_OUTPUT_DIR to it; locally the same variable points at a
scratch directory. The file holds exactly one line of plain text.
"""

import os
from pathlib import Path

LINE = "Sorry boss, the council cut our water off till Thursday and I can't come in unwashed like this."

# The kit gate: 1 to 140 characters, at most 20 words, one line.
assert 1 <= len(LINE) <= 140, "line breaks the 140-character gate"
assert len(LINE.split()) <= 20, "line breaks the 20-word cap"
assert "\n" not in LINE, "line must stay on one line"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
