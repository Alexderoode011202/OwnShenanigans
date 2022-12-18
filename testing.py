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


plt.plot(line, line*2, "r", line, line**0.5, "b", line, line**2, "k")
# , "b", line, line**2, "k"
plt.axis([0,10, 0, 10])
plt.ylabel('some numbers')
plt.xlabel("I have no clue wtf I am doing here")
mpl.rcParams['lines.linestyle'] = '--'
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
