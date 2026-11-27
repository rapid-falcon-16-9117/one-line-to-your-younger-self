#!/usr/bin/env python3
"""One Line to Your Younger Self — writes the final line to entry.txt.

The entry is a single line a writer would send back to their younger self:
a bittersweet micro-story with a named person and a final image that stays.
The line below is the champion of a judge-simulator tournament run against
the brief's criteria in order (told to a younger self; only this older self
could say it; lands in one breath; carries a turn; honest and specific
enough to sting): an imperative addressed straight at the younger self,
one exact age, one brother, one last pickup, nine years of dialling a
number that never answers again.
"""

import os

LINE = "Call your brother back the night you turn twenty-one \u2014 it's the last time he picks up, and you'll keep dialling his number for nine years."


def main() -> None:
    # Self-check against the sealed gate: entry.txt must be UTF-8 text of
    # 1-200 characters, a single line, not only white space. The brief also
    # forbids a second sentence doing the work, so assert one line only.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars, got %d" % len(LINE)
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE and LINE.strip(), "entry must not be blank or padded"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt mismatch: %r" % written


if __name__ == "__main__":
    main()
