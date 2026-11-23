"""One Letter for Your Day: J (jetlagged).

Writes exactly one byte -- the letter J -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), no trailing newline.
Python 3.13, stdlib only.
"""

import os

LETTER = b"J"


def main() -> None:
    if len(LETTER) != 1 or not (b"A" <= LETTER <= b"Z"):
        raise ValueError("LETTER must be exactly one byte A-Z")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
