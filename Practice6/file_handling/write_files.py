# Example 1: write to a file
f = open("demofile.txt", "w")
f.write("Hello! Welcome to the file.")
f.close()

# Example 2: overwrite file content
f = open("demofile.txt", "w")
f.write("This content replaces the previous text.")
f.close()

# Example 3: append to file
f = open("demofile.txt", "a")
f.write("\nThis line is appended.")
f.close()

# Example 4: append another line
f = open("demofile.txt", "a")
f.write("\nAppending another line.")
f.close()

# Example 5: create new file
f = open("newfile.txt", "x")
f.write("New file created.")
f.close()