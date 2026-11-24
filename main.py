"""One word for your Wi-Fi: Ghosting.

The stance, plainly: the router does not "drop" — it ghosts. Full bars,
"connected", then gone without a word, and back the moment I stop needing it.
Ghosting is the one word that is funny on sight and exactly true, and it needs
no explaining, which is the whole test.

Deterministic, no network, no randomness: /output/entry.txt is the same bytes
every run, and those bytes are the word alone (no trailing newline).
"""

import os

WORD = "Ghosting"


def main() -> None:
    # The sealed gate: 1-20 characters, one word of letters, not only whitespace.
    assert 1 <= len(WORD) <= 20, "the gate is 1-20 code points"
    assert WORD.isalpha(), "the gate wants one word of letters, nothing else"
    assert WORD == WORD.strip(), "no surrounding whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
