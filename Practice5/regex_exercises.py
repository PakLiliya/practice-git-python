import re

# 1. 'a' followed by zero or more 'b'
print("1:", re.fullmatch(r"ab*", "abbb"))

# 2. 'a' followed by 2-3 'b'
print("2:", re.fullmatch(r"ab{2,3}", "abb"))

# 3. lowercase joined with underscore
text = "hello_world test_string Invalid_String"
print("3:", re.findall(r"\b[a-z]+_[a-z]+\b", text))

# 4. One uppercase followed by lowercase
text = "Hello world Test Python"
print("4:", re.findall(r"\b[A-Z][a-z]+\b", text))

# 5. 'a' followed by anything ending in 'b'
print("5:", re.fullmatch(r"a.*b", "axxxb"))

# 6. Replace space, comma or dot with colon
text = "Hello, world. Python is fun"
print("6:", re.sub(r"[ ,.]", ":", text))

# 7. snake_case to camelCase
def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)

print("7:", snake_to_camel("hello_world_example"))

# 8. Split at uppercase letters
text = "SplitThisString"
print("8:", re.split(r"(?=[A-Z])", text))

# 9. Insert spaces before capital letters
text = "InsertSpacesHere"
print("9:", re.sub(r"(?<!^)(?=[A-Z])", " ", text))

# 10. camelCase to snake_case
def camel_to_snake(text):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()

print("10:", camel_to_snake("camelCaseExample"))