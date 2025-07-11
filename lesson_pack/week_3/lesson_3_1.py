# lesson3_1_collections_list_basics.py

# 1) Lesson header
print("Lesson 3.1 – Lists, Tuples, Sets & Strings: List Basics\n")

# 2) Creating lists
empty_list = []
primes = [2, 3, 5, 7, 11]
mixed = ["Alice", 42, True, 3.14]
print("List creation:")
print(" ▶ empty_list =", empty_list)
print(" ▶ primes     =", primes)
print(" ▶ mixed      =", mixed, "\n")

# 3) Accessing elements by index
print("Indexing:")
print(" ▶ primes[0]  =", primes[0])
print(" ▶ primes[-1] =", primes[-1], "(last element)\n")

# 4) Slicing lists
print("Slicing:")
print(" ▶ primes[1:4]   =", primes[1:4])
print(" ▶ primes[:3]    =", primes[:3])
print(" ▶ primes[2:]    =", primes[2:])
print(" ▶ primes[::2]   =", primes[::2], "(every other element)\n")

# 5) Modifying lists
print("Modifying:")
primes.append(13)
print(" ▶ After append(13):", primes)
primes.insert(2, 4)
print(" ▶ After insert(2, 4):", primes)
primes.remove(4)
print(" ▶ After remove(4):", primes)
last = primes.pop()
print(f" ▶ After pop(): removed {last}, list is now {primes}\n")

# 6) Iterating over a list
print("Iteration:")
for num in primes:
    print("  • prime:", num)
print()

# 7) List concatenation and repetition
a = [1, 2, 3]
b = ["x", "y"]
print("Concatenation & repetition:")
print(" ▶ a + b     =", a + b)
print(" ▶ b * 3     =", b * 3, "\n")

# 8) List comprehensions
print("List comprehensions:")
squares = [n ** 2 for n in range(6)]
evens = [n for n in range(10) if n % 2 == 0]
print(" ▶ squares =", squares)
print(" ▶ evens   =", evens, "\n")

# 9) Common list methods
print("Common methods:")
print(" ▶ len(primes)      =", len(primes))
print(" ▶ min(primes)      =", min(primes))
print(" ▶ max(primes)      =", max(primes))
print(" ▶ primes.count(3)  =", primes.count(3))
print(" ▶ primes.index(7)  =", primes.index(7), "\n")
