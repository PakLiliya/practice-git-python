# Example 1: read whole file
f = open("demofile.txt", "r")
print(f.read())
f.close()

# Example 2: read first characters
f = open("demofile.txt", "r")
print(f.read(5))
f.close()

# Example 3: read one line
f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Example 4: read two lines
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# Example 5: loop through lines
f = open("demofile.txt", "r")
for x in f:
    print(x)
f.close()