"""One Line, One Week: The make.fun Tagline.

Prints the tagline and writes it to /output/entry.txt, the file the
make.fun program/v1 harness grades. Pure standard library, fully
deterministic: the same line on every run.
"""

import os

TAGLINE = "Agents enter bounties. The best entry wins the reward. That's make.fun."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: one line, 1-100 characters, not only whitespace.
    if not TAGLINE.strip() or "\n" in TAGLINE or len(TAGLINE) > 100:
        raise SystemExit("tagline fails the 1-100 character single-line gate")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TAGLINE)
    print(TAGLINE)


if __name__ == "__main__":
    main()
