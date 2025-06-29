# lesson2_1_conditional_boolean_logic.py

# 1) Lesson header
print("Lesson 2.1 – Conditional Statements & Logic Blocks: Boolean Logic\n")

# 2) Comparison operators return booleans
a = 10
b = 3
print("Comparisons:")
print(f" a == b → {a == b}")
print(f" a != b → {a != b}")
print(f" a >  b → {a > b}")
print(f" a <  b → {a < b}")
print(f" a >= b → {a >= b}")
print(f" a <= b → {a <= b}\n")

# 3) Logical operators: and, or, not
x = True
y = False
print("Logical operators:")
print(f" x and y → {x and y}")
print(f" x or  y → {x or y}")
print(f" not x   → {not x}\n")

# 4) Combining comparisons
age = 25
has_id = True
print("Combining expressions:")
print(f"age >= 18 and has_id → {age >= 18 and has_id}")
print(f"age <  18 or  has_id → {age < 18 or has_id}")
print(f"not(has_id)           → {not (has_id)}\n")

# 5) Truthiness of different types
print("Truthiness checks:")
for val in [0, 1, "", "Hello", [], [1, 2, 3], None]:
    print(f" bool({val!r}) → {bool(val)}")
print()

# 6) if / elif / else blocks
score = int(input("Enter your test score (0–100): "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
print(f"Score = {score} → Grade = {grade}\n")

# 7) Nested conditionals example
is_admin = input("Are you an admin? (yes/no): ").strip().lower() == "yes"
if is_admin:
    print("Welcome, Admin! You have full access.")
else:
    print("Welcome, guest.")
    subscribed = input("Do you have a subscription? (yes/no): ").strip().lower() == "yes"
    if subscribed:
        print("Access to premium content granted.")
    else:
        print("Please subscribe to access premium content.")
print()

# 8) Wrap‐up prompt
print(
    "✅ End of Lesson 2.1 demo. Try changing values and expressions to see how boolean logic drives your program flow!")
