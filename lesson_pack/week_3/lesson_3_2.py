# lesson3_2_collections_dicts_error_handling.py

# 1) Lesson header
print("Lesson 3.2 – Dictionaries & Error Handling: Dictionary Basics\n")

# 2) Creating dictionaries
empty_dict = {}
person = {
    "name": "Alice",
    "age": 30,
    "city": "London"
}
print("Dictionary creation:")
print(" ▶ empty_dict =", empty_dict)
print(" ▶ person     =", person, "\n")

# 3) Accessing values
print("Accessing values:")
print(" ▶ person['name']  =", person["name"])
print(" ▶ person.get('age')=", person.get("age"))
print(" ▶ person.get('job')=", person.get("job"), "(returns None if missing)\n")

# 4) Adding and updating entries
person["email"] = "alice@example.com"  # add new key
person["city"] = "Manchester"  # update existing key
print("After add/update:")
print(" ▶ person     =", person, "\n")

# 5) Removing entries
age = person.pop("age")  # removes and returns value
print("After pop('age') → removed age:", age)
# del person["job"]                        # would KeyError if key missing
print(" ▶ person now =", person, "\n")

# 6) Iterating over a dictionary
print("Iterating keys:")
for key in person:
    print("  •", key)
print("\nIterating key → value:")
for key, value in person.items():
    print(f"  • {key} → {value}")
print()

# 7) Nested dictionaries
team = {
    "Alice": {"role": "Developer", "level": 2},
    "Bob": {"role": "Designer", "level": 3}
}
print("Nested dictionary access:")
print(" ▶ team['Bob']['role'] =", team["Bob"]["role"], "\n")

# 8) Handling missing keys with try/except
print("Error handling with try/except:")
try:
    print(" ▶ team['Charlie'] →", team["Charlie"])
except KeyError as e:
    print(f" ⚠️ KeyError: '{e.args[0]}' not found in team\n")

# 9) Common dict methods
print("Common dict methods:")
print(" ▶ keys()    →", list(person.keys()))
print(" ▶ values()  →", list(person.values()))
print(" ▶ items()   →", list(person.items()))
print(" ▶ 'email' in person →", "email" in person, "\n")
