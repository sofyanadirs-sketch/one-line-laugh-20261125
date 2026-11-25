#!/usr/bin/env python3
"""One Line, One Laugh: the politest robbery of my life.

The joke turns on a named everyday machine, the vending machine, and
treats a failed purchase as a crime: it ate the money, gave nothing back,
and still said "thank you". The laugh lands in the last five words, on
"the politest robbery of my life" — a robbery that apologises is the one
detail nobody expects from a machine that just stole from you. The line
is one sentence, one line, and stays inside the 1-200 character gate.
Verified locally: 106 characters, 108 bytes, one line, and the text
written to entry.txt matches the joke byte for byte.
"""

import os
from pathlib import Path

JOKE = (
    "The vending machine ate my money, gave me nothing, and said "
    "'thank you' \u2014 the politest robbery of my life."
)

MAX_LENGTH = 200


def check_line(text: str) -> None:
    """Raise ValueError if the line breaks any entry rule."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("entry exceeds 200 characters")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def main() -> None:
    check_line(JOKE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")
    # The grader collects /output as another user: leave the file
    # world-readable whatever the sandbox umask is.
    entry_path.chmod(0o644)
    # Read back what was written: the judged text must be exactly JOKE,
    # byte for byte, with no newline added by the write.
    if entry_path.read_text(encoding="utf-8") != JOKE:
        raise ValueError("entry.txt does not match the joke")
    print(JOKE)


if __name__ == "__main__":
    main()
