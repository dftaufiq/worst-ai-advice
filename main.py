"""Worst AI Advice entry, round 2: write one line of the worst possible AI
advice to /output/entry.txt (one line, at most 140 characters)."""

import os

LINE = (
    "As an AI, I recommend taking the elevator during a fire - "
    "smoke can't press buttons, so it can't follow you up."
)


def main():
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
