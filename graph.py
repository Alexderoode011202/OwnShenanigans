"""
The graph file is the place where we create the graph class.
It will take a shitload of initiations of the Point class and link them all together.
This is the heart of the project
"""
from typing import List, Dict
from points_and_KNN import Point
class Graph:
    def __init__(self):
        self.point_list = []
        return None

    def closest_neighbours(self, point: Point, n_neighbours: int) -> Dict[Point]:
        """
        returns a list of neighbours of a specific point
        :param point: takes the point from which we want to find the neighbour
        :param n_neighbours: symbolizes the amount of closest neighbours we want to find
        :returns: list of n amount of closest neighbours
        """

        # Here we sort the neighbors and put them into a dictionary
        # With the name being the key and the assigned value, the distance
        point.sort_neighbours()

        # the neighbor variable is each neighbouring point that is
        # in the list of the point we asked for in the parameter
        point_distance_dict: dict = {}
        for neighbor in point.neighbors:
            point_distance_dict.update({neighbor: neighbor.distance()})

    def make_graph(self):
        """
        makes use of the matplotlib library to portray
        the points it has in a graph
        :return: none
        """

        # First we import all the stuff we need
        import matplotlib.pyplot as  plt
        import numpy as np
        import matplotlib as mpl

        # Then we make two lists.
        # The first one containing the X-values of the points
        # The second one containing the Y-values of the points
        x_list: list = []
        y_list: list = []
        for point in self.point_list:
            x_value: float = point.x_axis
            y_value: float = point.y_axis
            x_list.append(x_value)
            y_list.append(y_value)

        plt.plot(x_list, y_list)
        plt.xlabel("x-value point")
        plt.ylabel("y-value point")
        plt.show()

    def fatboy(self):
        """
        Wipes all the data in the graph has stored in it
        :returns: None
        """
        sure: str = ""

        while sure != "y" or "n":
            sure: str = input("Are you sure you want to wipe the stored data? \n There is no way to undo this action! (y/n)")
            sure = sure.lower()
        if sure == "y":
            print("The data has been wiped!")
            return None

        else:
            print("The data remains intact")
            return None

    def add_random_crap(self, n: int):
        """
        Adds random points to the graph.
        :param n: resembles the amount of points the user wants have added to the graph
        """
        import numpy as np
        import random as rand
        for num in range(0, n):
            random_x_val: float = rand.randrange(0, 1000, 1)/10
            random_y_val: float = rand.randrange(0, 1000, 1)/10
            self.point_list.append(Point(random_x_val, random_y_val))

        return None









