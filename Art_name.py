#!/usr/bin/env python3
"""
Colourful ASCII Art Banner (no pyfiglet)
Created by Tanaka Mucheke
"""

import sys
import random
from colorama import init, Fore, Style

init(autoreset=True)

# ========== Character patterns (5 lines high, 5-6 chars wide) ==========
# Each character is represented as a list of 5 strings
CHAR_MAP = {
    'A': [
        " ███ ",
        "█   █",
        "█████",
        "█   █",
        "█   █"
    ],
    'B': [
        "████ ",
        "█   █",
        "████ ",
        "█   █",
        "████ "
    ],
    'C': [
        " ███ ",
        "█   ",
        "█   ",
        "█   ",
        " ███ "
    ],
    'D': [
        "████ ",
        "█   █",
        "█   █",
        "█   █",
        "████ "
    ],
    'E': [
        "█████",
        "█    ",
        "████ ",
        "█    ",
        "█████"
    ],
    'F': [
        "█████",
        "█    ",
        "████ ",
        "█    ",
        "█    "
    ],
    'G': [
        " ███ ",
        "█    ",
        "█ ███",
        "█   █",
        " ███ "
    ],
    'H': [
        "█   █",
        "█   █",
        "█████",
        "█   █",
        "█   █"
    ],
    'I': [
        "█████",
        "  █  ",
        "  █  ",
        "  █  ",
        "█████"
    ],
    'J': [
        "█████",
        "   █ ",
        "   █ ",
        "█  █ ",
        " ██  "
    ],
    'K': [
        "█   █",
        "█  █ ",
        "███  ",
        "█  █ ",
        "█   █"
    ],
    'L': [
        "█    ",
        "█    ",
        "█    ",
        "█    ",
        "█████"
    ],
    'M': [
        "█   █",
        "██ ██",
        "█ █ █",
        "█   █",
        "█   █"
    ],
    'N': [
        "█   █",
        "██  █",
        "█ █ █",
        "█  ██",
        "█   █"
    ],
    'O': [
        " ███ ",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    'P': [
        "████ ",
        "█   █",
        "████ ",
        "█    ",
        "█    "
    ],
    'Q': [
        " ███ ",
        "█   █",
        "█   █",
        "█  █ ",
        " ███ "
    ],
    'R': [
        "████ ",
        "█   █",
        "████ ",
        "█   █",
        "█   █"
    ],
    'S': [
        " ███ ",
        "█    ",
        " ███ ",
        "    █",
        " ███ "
    ],
    'T': [
        "█████",
        "  █  ",
        "  █  ",
        "  █  ",
        "  █  "
    ],
    'U': [
        "█   █",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    'V': [
        "█   █",
        "█   █",
        "█   █",
        " █ █ ",
        "  █  "
    ],
    'W': [
        "█   █",
        "█   █",
        "█ █ █",
        "██ ██",
        "█   █"
    ],
    'X': [
        "█   █",
        " █ █ ",
        "  █  ",
        " █ █ ",
        "█   █"
    ],
    'Y': [
        "█   █",
        " █ █ ",
        "  █  ",
        "  █  ",
        "  █  "
    ],
    'Z': [
        "█████",
        "   █ ",
        "  █  ",
        " █   ",
        "█████"
    ],
    ' ': [  # space
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ],
    '0': [
        " ███ ",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    '1': [
        "  █  ",
        " ██  ",
        "  █  ",
        "  █  ",
        " ███ "
    ],
    '2': [
        " ███ ",
        "   █ ",
        " ███ ",
        "█    ",
        "█████"
    ],
    '3': [
        "█████",
        "    █",
        " ███ ",
        "    █",
        "█████"
    ],
    '4': [
        "█   █",
        "█   █",
        "█████",
        "    █",
        "    █"
    ],
    '5': [
        "█████",
        "█    ",
        "█████",
        "    █",
        "█████"
    ],
    '6': [
        " ███ ",
        "█    ",
        "████ ",
        "█   █",
        " ███ "
    ],
    '7': [
        "█████",
        "    █",
        "   █ ",
        "  █  ",
        " █   "
    ],
    '8': [
        " ███ ",
        "█   █",
        " ███ ",
        "█   █",
        " ███ "
    ],
    '9': [
        " ███ ",
        "█   █",
        " ████",
        "    █",
        " ███ "
    ]
}

def text_to_banner(text):
    """Convert a string into a list of 5 lines (each line is a string)."""
    text = text.upper()
    lines = ["" for _ in range(5)]
    for ch in text:
        pattern = CHAR_MAP.get(ch, CHAR_MAP[' '])
        for i in range(5):
            lines[i] += pattern[i] + "  "  # add two spaces between chars
    return lines

def main():
    print(Style.BRIGHT + Fore.CYAN + "\n✨ COLOURFUL ASCII ART BANNER (no pyfiglet) ✨" + Style.RESET_ALL)
    name = input(Fore.YELLOW + "Enter text: " + Style.RESET_ALL).strip()
    if not name:
        print(Fore.RED + "No text entered. Exiting.")
        return

    banner_lines = text_to_banner(name)

    # Colour each line randomly
    COLOURS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
               Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX,
               Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]

    for line in banner_lines:
        colour = random.choice(COLOURS)
        print(colour + line + Style.RESET_ALL)

    # Extra newlines to avoid phone case covering the bottom
    print("\n" * 3)

    # Watermark
    print(Style.DIM + Fore.CYAN + "Made by Tanaka Mucheke" + Style.RESET_ALL)

if __name__ == "__main__":
    main()