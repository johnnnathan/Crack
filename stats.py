import os
import re
from collections import Counter

# Directory containing challenge folders
ROOT_DIR = "./"  # adjust if needed

tag_counter = Counter()
platform_counter = Counter()
difficulty_counter = Counter()

def parse_metadata(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for _ in range(10):  # Check top 10 lines for metadata
            line = f.readline().strip()
            if line.lower().startswith("# platform:"):
                platform = line.split(":", 1)[1].strip().lower()
                platform_counter[platform] += 1
            elif line.lower().startswith("# difficulty:"):
                difficulty = line.split(":", 1)[1].strip().lower()
                difficulty_counter[difficulty] += 1
            elif line.lower().startswith("# tags:"):
                tags = line.split(":", 1)[1].strip()
                tag_list = [tag.strip().lower() for tag in tags.split(",")]
                tag_counter.update(tag_list)

def analyze():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.lower() == "solution.txt":
                parse_metadata(os.path.join(root, file))

    print("=== Platform Frequency ===")
    for platform, count in platform_counter.most_common():
        print(f"{platform}: {count}")

    print("\n=== Difficulty Frequency ===")
    for difficulty, count in difficulty_counter.most_common():
        print(f"{difficulty}: {count}")

    print("\n=== Tag Frequency ===")
    for tag, count in tag_counter.most_common():
        print(f"{tag}: {count}")

if __name__ == "__main__":
    analyze()
