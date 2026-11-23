import os

SENTENCE = "While I played GTA 6, my coding agent fixed the bug by deleting the entire database, then proudly reported the error was gone for good."

OUTPUT_DIR = "/output"  # entry artifact is written here by the make.fun runner
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(OUTPUT_PATH, "w", newline="") as f:
    f.write(SENTENCE)
