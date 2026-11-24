"""Worst AI Advice entry: write one line of the worst possible AI advice
to /output/entry.txt (one line, at most 140 characters)."""

import os

LINE = (
    "As an AI, I recommend microwaving your phone for 30 seconds "
    "to kill the virus - the sparks mean it is working."
)


def main() -> None:
    # Gate self-check: one line, 1-140 characters, not whitespace-only.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry violates the gate"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
