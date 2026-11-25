#!/usr/bin/env python3
"""Write one original joke about Monday mornings for make.fun.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.

Why this joke works: an alarm clock is a machine that shouts, so giving
it a quiet civil-service job instead — serving formal paperwork on the
sleeper's dreams — flips the expected noise into silence. The dreams
become noisy tenants, Monday becomes the neighbour who complains in
writing, and the whole week starts with a form to fill in before coffee.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_line() -> str:
    """Return the entry line.

    The alarm never rings; it files paperwork instead. The twist is
    that the dreams, not the sleeper, are the ones making the noise,
    so Monday arrives as a bureaucrat rather than a bell.
    """
    return (
        "My Monday alarm doesn't ring. "
        "It files a noise complaint against my dreams."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-200 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what the grader reads must be exactly the line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "entry.txt round-trip mismatch"
    print(LINE)


if __name__ == "__main__":
    main()
