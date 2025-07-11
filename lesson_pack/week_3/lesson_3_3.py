# lesson3_3_files_numpy_read_write.py

"""
Lesson 3.3 – Files & NumPy: Read/Write Files

Covers:
 1) Reading and writing plain text files
 2) CSV file I/O with the csv module
 3) NumPy array read/write (txt & binary .npy)
"""

import csv
import numpy as np

# 1) Reading a plain text file
print("1) Reading a text file (example.txt):")
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(" ▶ Contents of example.txt:")
    for line in lines:
        print("   ", line.rstrip())
except FileNotFoundError:
    print(" ⚠️ example.txt not found. Create it with some sample lines.\n")
else:
    print()

# 2) Writing to a plain text file
print("2) Writing to a text file (output.txt):")
data_lines = ["Line one", "Line two", "Line three"]
with open("output.txt", "w", encoding="utf-8") as f:
    for ln in data_lines:
        f.write(ln + "\n")
print(" ▶ Wrote 3 lines to output.txt\n")

# 3) CSV I/O using csv module
print("3) CSV read/write (data.csv):")
rows = [
    ["name", "age", "score"],
    ["Alice", "30", "88.5"],
    ["Bob", "25", "92.0"],
    ["Carol", "27", "79.3"],
]
# Write CSV
with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
print(" ▶ Written data.csv with headers and 3 rows")

# Read CSV
with open("data.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    print(" ▶ Reading back data.csv:")
    for r in reader:
        print("   ", r)
print()

# 4) NumPy: reading & writing text
print("4) NumPy read/write (txt):")
arr = np.arange(1, 10).reshape(3, 3)
print(" ▶ Original array:\n", arr)
# Save as text
np.savetxt("array.txt", arr, fmt="%d", delimiter=",")
print(" ▶ Saved array to array.txt")
# Load from text
loaded = np.loadtxt("array.txt", delimiter=",", dtype=int)
print(" ▶ Loaded from array.txt:\n", loaded, "\n")

# 5) NumPy: binary format .npy
print("5) NumPy read/write (binary .npy):")
# Save binary
np.save("array.npy", arr)
print(" ▶ Saved array to array.npy")
# Load binary
loaded_npy = np.load("array.npy")
print(" ▶ Loaded from array.npy:\n", loaded_npy, "\n")
