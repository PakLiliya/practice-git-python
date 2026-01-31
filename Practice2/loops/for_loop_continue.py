# Example 1: continue in for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Example 2
for x in range(6):
    if x == 3:
        continue
    print(x)

# Example 3
for x in "banana":
    if x == "a":
        continue
    print(x)

# Example 4
numbers = [1, 2, 3, 4]
for n in numbers:
    if n == 2:
        continue
    print(n)

# Example 5
for x in range(5):
    if x == 1:
        continue
    print(x)
