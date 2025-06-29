# lesson2_2_loops_for.py

# 1) Lesson header
print("Lesson 2.2 – Loops & Iteration Patterns: for Loops\n")

# 2) Basic for-loop over a list
fruits = ["apple", "banana", "cherry"]
print("Iterating over a list:")
for fruit in fruits:
    print("  –", fruit)
print()

# 3) Looping over a range of numbers
print("Using range():")
for i in range(5):  # 0, 1, 2, 3, 4
    print("   index", i)
print()

print("Using range(start, stop, step):")
for i in range(2, 10, 3):  # 2, 5, 8
    print("   step 3:", i)
print()

# 4) Iterating over a string (characters)
word = "Python"
print("Characters in string:")
for ch in word:
    print("  *", ch)
print()

# 5) Looping through a dictionary
person = {"name": "Alice", "age": 30, "city": "London"}
print("Dictionary iteration (key → value):")
for key, value in person.items():
    print(f"  {key} → {value}")
print()

# 6) Using enumerate() to get index + item
colors = ["red", "green", "blue"]
print("Using enumerate():")
for idx, color in enumerate(colors, start=1):
    print(f"  {idx}. {color}")
print()

# 7) Nested loops
print("Nested loops (pairwise sums):")
numbers = [1, 2, 3]
for x in numbers:
    for y in numbers:
        print(f"  {x} + {y} = {x + y}")
print()

# 8) break and continue
print("break & continue examples:")
for i in range(1, 10):
    if i == 5:
        print("   breaking at", i)
        break
    if i % 2 == 0:
        continue
    print("   odd number:", i)
print()

# 9) Loop else clause
print("for-else (runs when loop isn’t broken):")
for n in [2, 3, 5, 7]:
    print("  checking", n)
    if n == 4:
        print("  found a 4!")
        break
else:
    print("  loop completed without finding a 4")
print()

# 10) List comprehensions (compact loop)
print("List comprehension vs. loop:")
squares = [i ** 2 for i in range(6)]
print("  squares =", squares, "\n")

# 11) Wrap-up
print(
    "✅ End of Lesson 2.2 demo. Experiment by changing the collections and loop logic to see how each pattern behaves!")
