"""
In this file we focus on creating points, graphs, and trying to apply a KNN machine
learning algorithm with minimal use, just cuz I can.
"""
import math
from typing import Tuple, List

class Point:

    def __init__(self, x_axis: float, y_axis) -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.neighbors: list = []

    def distance(self, other_point: object) -> float:
        """
        Is needed for checking the distance between a point and a different point module
        :param other_point: takes the other point we got to find the distance for
        :returns: float value containing the distance between the two points
        """
        x_distance: float = self.x_axis**2 + other_point.x_axis**2
        y_distance: float = self.y_axis**2 + other_point.y_axis**2
        distance = math.sqrt(x_distance + y_distance)
        return distance

    def as_tuple(self) -> Tuple[float, float]:
        """
        returns the point as a tuple
        :returns: the point in a tuple format
        """

        return self.x_axis, self.y_axis

    def sort_neighbours(self) -> None:
        """
        re-sorts the neighbour list of the point based on distance,
        with the closest one being first in the list
        :param: None
        :returns: None
        """

        distance_neighbour_dict: dict = {}
        new_distance_neighbour_list: list = []
        for point in self.neighbors:
            distance_neighbour_dict.update({point.distance(self): point})

        #distance_list = (distance_neighbour_dict.keys.sort())
        distance_list: list = []
        for key in distance_neighbour_dict.keys():
            distance_list.append(key)

        for distance in distance_list:
            new_distance_neighbour_list.append(distance_neighbour_dict[distance])

        return None

    def nearest_neighbours(self, n: int) -> List[object]:
        """
        Finds the n-amount of nearest neighbours
        :param n: takes the amount of nearest neighbours we want to look for
        :returns: list containing the n-amount of nearest neighbours
        """

    def add_neighbour(self, neighbour):
        """
        adds neighbour to the neighbour list
        :param neighbour: appends the neighbour in question to the neighbour list
        :returns: None
        """

        self.neighbors.append(neighbour)
        self.sort_neighbours()
        return None

    def __str__(self):
        """
        :returns: the point as a string with the x- and y-axis
        """
        return f"({self.x_axis},{self.y_axis})"

    def show_neighbours(self) -> List[object]:
        """
        shows all the linked neighbours of a point without getting the memory location in return
        :returns: list of linked neighbouring points
        """
        returned_list: list = []
        for neighbour in self.neighbors:
            returned_list.append(str(neighbour))

        return returned_list


""" 
Here we test whether the Point class and it's methods actually work
"""
test_point1 = Point(3, 3)
print(test_point1)

test_point2 = Point(5, 9)
print(test_point2)

test_point1.add_neighbour(test_point2)
print(test_point1.neighbors)

print(test_point1.show_neighbours())
