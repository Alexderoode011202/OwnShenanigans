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
# Converting dict.keys() to list
"""
test_dict: dict = {1: 2, 3: 4, 5: 6, 7: 8}
for keys in test_dict.keys():
    print(keys)

test_values = list(test_dict.values())
print(test_values)
# This does work!

test_list: list = [4,8,2,1,6]
print(min(test_list))
"""
# Tuple test
"""
print("another test")
from points_and_KNN import Point
import random
counter: int = 0
point_list: list = []
while counter != 10:
    point_list.append(Point(random.randrange(1, 11, 1), random.randrange(1,11,1)))
    counter +=1
for point in point_list:
    x, y = point.as_tuple()
    print(f"{x} and {y}")
"""

# Having multiple plots

# Try- Except statements

"""
def divided10() -> float:
    try: first_num: int = int(input("choose a number between 1 and 10"))
    except ValueError:
        print("I dunno what to do")
        return None

    else:
        return first_num/10


divided10()
"""

test_dict: dict = {"A": "a", "B": "B"}

new_dict = dict(A="yea", B="Nope")
print(new_dict.items())
print(type(new_dict.items()))