# Example 1: break in while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Example 2
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# Example 3
n = 1
while True:
    print(n)
    if n == 3:
        break
    n += 1

# Example 4
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1

# Example 5
while True:
    print("Stop")
    break
