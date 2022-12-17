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





