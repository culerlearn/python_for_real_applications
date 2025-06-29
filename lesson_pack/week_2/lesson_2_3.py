# lesson2_3_functions_scope_reusability.py

# 1) Lesson header
print("Lesson 2.3 – Functions, Scope & Reusability: Function Basics\n")


# 2) Defining a simple function
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


print("Simple function:")
print(" ▶", greet("Alice"), "\n")


# 3) Functions with parameters and return values
def add(a, b):
    """Return the sum of a and b."""
    return a + b


def multiply(a, b=1):
    """Return a * b; uses default b=1 if not provided."""
    return a * b


print("Parameters & defaults:")
print(" ▶ add(4, 5)       =", add(4, 5))
print(" ▶ multiply(7, 3)  =", multiply(7, 3))
print(" ▶ multiply(7)     =", multiply(7), "\n")

# 4) Keyword arguments
print("Keyword arguments:")
print(" ▶ add(b=10, a=3)  =", add(b=10, a=3), "\n")


# 5) Variable positional & keyword args
def summarize(title, *items, **metadata):
    """Print a summary with a title, list of items, and metadata dict."""
    print(f"Summary: {title}")
    print(" Items:")
    for it in items:
        print("  -", it)
    print(" Metadata:", metadata)
    print()


print("Variable args:")
summarize("Fruits", "apple", "banana", count=2, source="local")

# 6) Function scope: local vs. global
message = "global"


def scope_demo():
    message = "local"
    print(" Inside function, message =", message)


print("Scope demo:")
scope_demo()
print(" Outside function, message =", message, "\n")

# 7) Docstrings and introspection
print("Docstring for add():")
print(add.__doc__, "\n")


# 8) Higher-order functions (passing function as argument)
def shout(text):
    return text.upper() + "!"


def apply_twice(func, value):
    """Call func on value twice."""
    return func(func(value))


print("Higher-order function:")
print(" ▶", apply_twice(shout, "echo"), "\n")

# 9) Anonymous (lambda) functions
doubles = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print("Lambda with map():")
print(" ▶ doubles =", doubles, "\n")

# 10) Wrap-up prompt
print(
    "✅ End of Lesson 2.3 demo. Try defining your own functions, experimenting with args, scope, and returning values!")
