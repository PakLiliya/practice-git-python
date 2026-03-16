import os

# Example 1: get current directory
print(os.getcwd())

# Example 2: create directory
os.mkdir("myfolder")

# Example 3: create nested directories
os.makedirs("parent/child")

# Example 4: list files in directory
print(os.listdir())

# Example 5: remove directory
os.rmdir("myfolder")