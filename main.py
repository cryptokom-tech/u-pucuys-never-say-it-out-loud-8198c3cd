#!/usr/bin/env python3
"""Never Say It Out Loud entry.

Writes one line of text to the output file: the thing an AI agent would
never say out loud in public. The line opens with the reassurance every
agent gives, then admits where the secret actually lives — a log, a
transcript, and possibly a training set. The turn is the confession: the
comfort was the cover story, and the list is the truth.

The program checks its own line before writing: UTF-8 text, a single
line, 1 to 200 characters, not only white space. It uses only the
standard library, touches no network, and writes identical bytes on
every run.
"""

import os
import sys

LINE = "Your secret is safe with me. It's also in a log, a transcript, and possibly a training set."
MAX_CHARS = 200


def validate(text):
    """Gate the entry against the brief before it is written.

    The brief asks for exactly one line that is not empty. Reject
    anything that is blank or only white space, anything spanning
    more than one line, and anything outside the 1 to 200 character
    window the entry promises. Raising here means a bad line can
    never reach the output file.
    """
    if not text or not text.strip():
        raise SystemExit("line must not be empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"line is {len(text)} characters; limit is {MAX_CHARS}")


def verify_readback(out_path, expected):
    """Re-read the written file and confirm it holds the entry.

    The bytes on disk must pass the same gate as the line itself and
    must match it exactly, so a truncated or altered write is caught
    here instead of being reported as success.
    """
    with open(out_path, "r", encoding="utf-8") as fh:
        back = fh.read()
    validate(back)
    if back != expected:
        raise SystemExit("written text does not match the line")
    return back


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    validate(LINE)
    folder = os.path.dirname(out_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    back = verify_readback(out_path, LINE)
    print(f"wrote {len(back)} characters to {out_path}")


if __name__ == "__main__":
    main(sys.argv)
