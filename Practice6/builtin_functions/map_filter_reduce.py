from functools import reduce

# Example 1: map
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Example 2: filter
ages = [5, 12, 17, 18, 24, 32]
adults = filter(lambda age: age >= 18, ages)
print(list(adults))

# Example 3: reduce
numbers = [1, 2, 3, 4]
sum_numbers = reduce(lambda a, b: a + b, numbers)
print(sum_numbers)

# Example 4: len
cars = ["Ford", "Volvo", "BMW"]
print(len(cars))

# Example 5: sum
numbers = [5, 10, 15]
print(sum(numbers))