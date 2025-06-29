import matplotlib.pyplot as plt

"""
Lesson 4.1 – Matplotlib Basics & Charting: Why Visualize?

Covers:
 1) Importing Matplotlib
 2) Creating simple line, bar, and scatter plots
 3) Understanding when to use each chart type
"""

# 2. Creating a Line Plot ####################################

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
#
# plt.plot(x, y)
# plt.title("Simple Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# 3. Creating a Bar Chart ####################################
# categories = ['A', 'B', 'C']
# values = [5, 7, 3]
#
# plt.bar(categories, values)
# plt.title("Bar Chart Example")
# plt.show()

# 4. Creating a Histogram ####################################
# import numpy as np
#
# data = np.random.randint(1, 100, 50)
# plt.hist(data, bins=10)
# plt.title("Histogram of Random Data")
# plt.xlabel("Range")
# plt.ylabel("Frequency")
# plt.show()

# 5. Customizing Charts ####################################

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# plt.plot(x, y, label='Data Series')
# plt.legend()
# plt.show()

# 6. Saving a Chart ####################################

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# plt.legend()
# plt.plot(x, y, label='Data Series')
# plt.savefig("sample_chart.png")

# lesson4_1_matplotlib_basics_why_visualize.py


import matplotlib.pyplot as plt

# 1) Why visualize?
print("Lesson 4.1 – Why Visualize?\n")
print("Visualizations help us:")
print(" • Spot trends over time")
print(" • Compare categories at a glance")
print(" • Reveal relationships between variables\n")

# Sample data for demonstration
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [150, 200, 180, 220, 210, 240]
expenses = [80, 90, 95, 100, 105, 110]
customers = [30, 45, 40, 50, 48, 55]

# 2) Line plot: trends over time
plt.figure()
plt.plot(months, sales, marker='o', label="Sales")
plt.plot(months, expenses, marker='s', label="Expenses")
plt.title("Monthly Sales vs. Expenses")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 3) Bar chart: comparing categories
plt.figure()
x = range(len(months))
plt.bar(x, sales, width=0.4, label="Sales")
plt.bar([i + 0.4 for i in x], expenses, width=0.4, label="Expenses")
plt.xticks([i + 0.2 for i in x], months)
plt.title("Sales & Expenses by Month")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()

# 4) Scatter plot: relationships
plt.figure()
plt.scatter(customers, sales)
plt.title("Sales vs. Number of Customers")
plt.xlabel("Number of Customers")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.show()

# 5) Wrap-up prompt
print("✅ End of Lesson 4.1 demo. Ask students:")
print(" • Which chart best shows seasonal trends?")
print(" • How would you visualize profit = sales – expenses?")
print(" • Try adding a new dataset or changing markers/styles!")
