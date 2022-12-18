"""
Here we test whether relatively basic stuff works cuz I forgot.
And also mess around with foreign libraries
"""

import matplotlib as mpl

import numpy as np
import math
import matplotlib.pyplot as plt
"""
# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()

test = plt
test.show()

"""
line = np.arange(0,10,0.01)
smaller_line = np.arange(0,10,1)


plt.plot(line, line*2, color="r", linestyle="--")# , marker="3")
plt.plot(line, line**0.5, color="b", linestyle=":")# , marker="1")
plt.plot(smaller_line, smaller_line**2, color="k", marker=">", linestyle=":")
plt.plot(4, 40, marker="o")
# , "b", line, line**2, "k"
plt.axis([0,10, 0, 50])
plt.title("little experiment")
plt.ylabel('some numbers')
plt.xlabel("I have no clue wtf I am doing here")
plt.legend()
plt.show()



"""
fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

print(fig)
"""

# Dictionary stuffies
"""
dic: dict = {1: 2, 3: 4, 5: 6}
print(dic.keys())
empty_list: list = []
for key in dic.keys():
    print(key)
    empty_list.append(key)

print(empty_list)
"""
