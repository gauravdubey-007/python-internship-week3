"""Q2: Merge two text files into one."""

import os

folder = os.path.dirname(os.path.abspath(__file__))
file_a = os.path.join(folder, "file1.txt")
file_b = os.path.join(folder, "file2.txt")
output = os.path.join(folder, "merged.txt")

try:
    with open(file_a, "r", encoding="utf-8") as a, open(file_b, "r", encoding="utf-8") as b:
        content_a = a.read()
        content_b = b.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
else:
    with open(output, "w", encoding="utf-8") as out:
        out.write(content_a)
        if content_a and not content_a.endswith("\n"):
            out.write("\n")
        out.write(content_b)
    print("Files merged into merged.txt")
    print("--- merged.txt ---")
    print(open(output, encoding="utf-8").read())
