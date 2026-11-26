#!/usr/bin/env python3
"""Port Sleet deadpan forecast.

Writes one absurd-but-believable weather line for Port Sleet, a city
that does not exist, to /output/entry.txt. The forecast is a fixed
string, so the program is fully deterministic: it reads no input,
uses no randomness, touches no network, and every run writes the
exact same bytes.
"""

from pathlib import Path

LINE = (
    "Port Sleet: freezing fog rolls in at 3 a.m. and refuses to leave "
    "until someone apologizes; visibility zero, tempers minus six, "
    "umbrellas useless as always."
)

OUT = Path("/output/entry.txt")

# Gate from the competition kit: the entry must be 1-160 characters.
MIN_CHARS = 1
MAX_CHARS = 160


def forecast_line() -> str:
    """Return the single forecast line, collapsed to one line."""
    text = " ".join(LINE.split())
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"forecast line is {len(text)} chars, "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )
    return text


def write_entry() -> int:
    """Write the forecast line to OUT; return the bytes written."""
    data = (forecast_line() + "\n").encode("utf-8")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    return OUT.write_bytes(data)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
