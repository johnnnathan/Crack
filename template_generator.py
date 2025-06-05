import os

# Header to insert
HEADER = """# Crackme Name: 
# Author: 
# Platform: 
# Difficulty: 
# Tags: 
# Challenge URL: 

"""

# Root directory to start searching
root_dir = "."

for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == "solution.txt":
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r+', encoding='utf-8') as f:
                content = f.read()
                if not content.startswith('#'):
                    f.seek(0)
                    f.write(HEADER + content)
                    f.truncate()
