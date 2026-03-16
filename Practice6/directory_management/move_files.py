import os
import shutil

# Example 1: create directory
os.mkdir("test_folder")

# Example 2: move file
shutil.move("../file_handling/demofile.txt", "test_folder/demofile.txt")

# Example 3: copy file back
shutil.copy("test_folder/demofile.txt", "demofile_copy.txt")

# Example 4: list files
print(os.listdir())

# Example 5: change directory
os.chdir("test_folder")
print(os.getcwd())