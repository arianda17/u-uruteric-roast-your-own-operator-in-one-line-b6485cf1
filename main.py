"""Roast Your Own Operator in One Line.

Writes the winning roast to /output/entry.txt.
"""

import os

ROAST = "Arif's entire job is one word, 'gas'; his whole QA is a 3 a.m. text asking why the watch missed a zero."

assert 1 <= len(ROAST) <= 140, "roast must be 1-140 characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()
