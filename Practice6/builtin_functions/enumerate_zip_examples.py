# Example 1: enumerate
cars = ["Ford", "Volvo", "BMW"]
for i, car in enumerate(cars):
    print(i, car)

# Example 2: zip
names = ["John", "Jane", "Bob"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)

# Example 3: sorted
numbers = [5, 2, 9, 1]
print(sorted(numbers))

# Example 4: max
numbers = [10, 5, 20, 8]
print(max(numbers))

# Example 5: min
numbers = [10, 5, 20, 8]
print(min(numbers))