"""Rename the Planet: print the one-line entry from entry.txt."""

from pathlib import Path

PLANETS = (
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
)

MAX_CHARS = 200


def load_entry() -> str:
    path = Path(__file__).with_name("entry.txt")
    return path.read_text(encoding="utf-8")


def validate_entry(line: str) -> str:
    """Enforce the gate: one non-blank line, 1 to 200 characters."""
    if not line:
        raise SystemExit("entry.txt is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry contains control characters")
    if not any(planet in line for planet in PLANETS):
        raise SystemExit("entry names no planet of our solar system")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over 200")
    return line


def main() -> None:
    line = validate_entry(load_entry().strip())
    print(line)


if __name__ == "__main__":
    main()
