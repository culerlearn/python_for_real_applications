# lesson1_3_input_operators_logic_arithmetic.py

# 1) Lesson header
print("Lesson 1.3: Input, Operators & Basic Logic – Arithmetic Operators\n")

# 2) Reading user input
#    input() always returns a string
a_str = input("Enter the first number (a): ")
b_str = input("Enter the second number (b): ")

# 3) Converting inputs to numbers
#    You can use int() for whole numbers or float() for decimals
a = float(a_str)
b = float(b_str)
print(f"\na = {a} (type: {type(a).__name__})")
print(f"b = {b} (type: {type(b).__name__})\n")

# 4) Basic arithmetic operations
print("Arithmetic operations:")
print(f" a + b = {a + b}")
print(f" a - b = {a - b}")
print(f" a * b = {a * b}")
print(f" a / b = {a / b}       # true division")
print(f" a // b = {a // b}     # floor division")
print(f" a % b = {a % b}       # modulus (remainder)")
print(f" a ** b = {a ** b}     # exponentiation\n")

# 5) Operator precedence
#    *, /, //, %, ** before + and -
expr1 = a + b * 2
expr2 = (a + b) * 2
print("Operator precedence:")
print(f" a + b * 2      = {expr1}   # multiplication first")
print(f"(a + b) * 2     = {expr2}   # parentheses override\n")

# 6) Compound assignment
c = a  # start with a copy of a
c += b
print("Compound assignment:")
print(f" c = a; c += b → c = {c}")
c *= 2
print(f" c *= 2       → c = {c}\n")

# 7) Mixing types and error demonstration
#    Uncommenting the following line will raise TypeError
# print("a + b as strings: " + a_str + b_str)
