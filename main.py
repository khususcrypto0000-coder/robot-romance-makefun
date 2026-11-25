import os
import sys

ENTRY = "I said your name once and every smart speaker in the house lit up \u2014 even the one I never plugged in."

OUT_PATH = "/output/entry.txt"


def main():
    # GATE guards: 1-200 chars, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "ENTRY must be 1-200 characters"
    assert ENTRY.strip(), "ENTRY must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "ENTRY must be a single line"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "entry.txt is not byte-identical to ENTRY"
    print(ENTRY)


if __name__ == "__main__":
    main()
