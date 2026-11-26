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


def forecast_line() -> str:
    """Return the single forecast line, collapsed to one line."""
    text = " ".join(LINE.split())
    if not 1 <= len(text) <= 160:
        raise ValueError(f"forecast line is {len(text)} chars, must be 1-160")
    return text


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(forecast_line() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
