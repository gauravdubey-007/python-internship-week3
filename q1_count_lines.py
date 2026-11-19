"""Q1: Read a file and count total lines."""

import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file1.txt")

try:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"Total lines in file1.txt: {len(lines)}")
except FileNotFoundError:
    print("Error: file not found.")
