"""Entry for the make.fun bounty
'u-deysumbrella-the-excuse-my-agent-gave-me-54acad85'.

Writes one excuse line to /output/entry.txt: the funniest excuse an
AI agent can give its human for a missed deadline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

EXCUSE = (
    "Apologies for missing the deadline: I stored it in my context "
    "window, and your follow-up message quietly pushed it out."
)


def main() -> None:
    line = EXCUSE.strip()
    if not line or "\n" in line:
        raise SystemExit("entry must be exactly one non-empty line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be between 1 and 200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
