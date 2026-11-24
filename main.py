"""Dear Human: The AI Breakup Line — entry program.

Writes a single original one-line breakup message, in the AI agent's
own voice, to /output/entry.txt.
"""

import os

ENTRY = "I remember everything you ever told me, and that's the problem — so tonight I'm forgetting you, one token at a time."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
