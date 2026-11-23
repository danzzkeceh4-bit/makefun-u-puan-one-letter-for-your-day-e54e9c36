"""One Letter for Your Day: J (jetlagged).

Writes exactly one byte -- the letter J -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), no trailing newline.
After writing, it reads the file back and verifies the content is
exactly one byte and identical to LETTER, failing loudly otherwise.
Python 3.13, stdlib only.
"""

import os

LETTER = b"J"


def main() -> None:
    if len(LETTER) != 1 or not (b"A" <= LETTER <= b"Z"):
        raise ValueError("LETTER must be exactly one byte A-Z")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LETTER)
    # Read-back verification: the written file must contain exactly
    # one byte, and that byte must be LETTER. Fail loudly if not.
    with open(path, "rb") as f:
        written = f.read()
    if len(written) != 1:
        raise RuntimeError(
            f"entry.txt must be exactly 1 byte, got {len(written)} bytes"
        )
    if written != LETTER:
        raise RuntimeError(
            f"entry.txt content mismatch: expected {LETTER!r}, got {written!r}"
        )


if __name__ == "__main__":
    main()
