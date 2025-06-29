# 1) Comments and print
#    - Use `#` for single-line comments
#    - `print()` outputs to the console
print("Welcome to Lesson 1.2: Syntax, Variables & Data Types\n")

# 2) Variable assignment and naming rules
#    - Must start with a letter or underscore
#    - Case-sensitive: `count` ≠ `Count`
user_name = "Alice"
_count = 5
# invalid: 2nd_value = 10     # SyntaxError if uncommented
print("user_name:", user_name)
print("_count:", _count, "\n")

# 3) Basic data types
age = 30  # int
height_m = 1.75  # float
is_student = False  # bool
greeting = "Hello, world!"  # str

print("Types and values:")
print(" age       =", age, "| type:", type(age))
print(" height_m  =", height_m, "| type:", type(height_m))
print(" is_student=", is_student, "| type:", type(is_student))
print(" greeting  =", greeting, "| type:", type(greeting), "\n")

# 4) Multiple assignment
x, y, z = 1, 2.5, "three"
print("Multiple assignment → x, y, z =", x, y, z, "\n")

# 5) Basic arithmetic & string formatting
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b:.2f} = {a / b}")  # formatted to 2 decimals
print(f"{a} // {b} = {a // b}")  # integer division
print(f"{a} ** {b} = {a ** b}\n")  # exponent

# 6) Compound data types
#    - list, tuple, dict, set
favorite_numbers = [3, 7, 42]  # list (mutable)
dimensions = (1920, 1080)  # tuple (immutable)
person = {"name": "Alice",  # dict (key→value)
          "age": age,
          "student": is_student}
unique_ids = {101, 202, 303, 202}  # set (no duplicates)

print("favorite_numbers (list):", favorite_numbers)
print(" dimensions   (tuple):", dimensions)
print(" person       (dict):", person)
print(" unique_ids   (set) :", unique_ids, "\n")

# 7) Accessing & modifying
favorite_numbers.append(99)
print("After append:", favorite_numbers)
print("person['name']:", person["name"])
person["city"] = "London"
print("After add city:", person, "\n")

# 8) Indentation and code blocks
score = 85
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print(f"Score = {score} → Grade = {grade}\n")

# 9) Mixing types (and errors)
# Uncommenting the next line will raise a TypeError:
# print("Age plus name:", age + user_name)

# 10) Wrap up
print("▶︎ End of Lesson 1.2 demo. Feel free to modify and explore!")
