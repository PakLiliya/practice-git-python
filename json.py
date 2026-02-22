import json


# 1. Parse JSON (loads)

x = '{"name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["age"])


# 2. Convert Python to JSON (dumps)

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)


# 3. Convert Python types to JSON

print(json.dumps({"name": "John"}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))


# 4. Pretty print JSON

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(json.dumps(x, indent=4))


# 5. Sort JSON keys

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(json.dumps(x, indent=4, sort_keys=True))