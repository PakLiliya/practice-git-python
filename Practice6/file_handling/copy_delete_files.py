import shutil
import os

# Example 1: copy file
shutil.copy("demofile.txt", "copy_demofile.txt")

# Example 2: copy file with metadata
shutil.copy2("demofile.txt", "copy2_demofile.txt")

# Example 3: check if file exists
if os.path.exists("copy_demofile.txt"):
    print("File exists")

# Example 4: remove file
if os.path.exists("copy_demofile.txt"):
    os.remove("copy_demofile.txt")

# Example 5: remove second copy
if os.path.exists("copy2_demofile.txt"):
    os.remove("copy2_demofile.txt")