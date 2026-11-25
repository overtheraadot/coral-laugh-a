"""make.fun entry: One Line, One Laugh.

Writes a single hilarious line (at most 200 characters) to /output/entry.txt.
Python stdlib only.
"""

import os

# Revised: "attended" replaces "sat through" — it casts the cat as a formal
# reviewer, so the wordless laptop-shove exit lands as a verdict, not an
# accident. Shorter setup, same punchline: the turn is the joke (surprise),
# every word earns its place (economy), and a cat giving a code review by
# destroying the laptop is a fresh angle, not a stock cat joke.
ENTRY = "My cat attended my code review, knocked my laptop off the desk, and left \u2014 the most honest feedback I have ever received."


def verify(text):
    """Enforce the gate from RULES.txt: UTF-8, 1-200 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def write_entry(path="/output/entry.txt"):
    """Write ENTRY plus a trailing newline to path, creating the dir if needed."""
    verify(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    verify(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(ENTRY)
    path = write_entry()
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
