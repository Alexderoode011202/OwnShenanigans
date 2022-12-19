"""
The graph file is the place where we create the graph class.
It will take a shitload of initiations of the Point class and link them all together.
This is the heart of the project
"""

from points_and_KNN import Point
import random


class Graph:
    def __init__(self):
        self.point_list = []

    def closest_neighbours(self, n_neighbours: int) -> list:
        """
        returns a list of neighbours of a specific point
        :param n_neighbours: symbolizes the amount of closest neighbours we want to find
        :returns: list of n amount of closest neighbours
        """
        point_list: list = []
        point_dict: dict = {}
        distance_dict: dict = {}
        counter: int = len(self.point_list)-1

        for point in self.point_list:
            print(f"[{counter}] point: {point}")
            point_dict.update({counter: point})
            counter += 1

        # The input will be in the form of an integer, e.g. 55
        choice: int = int(input("Please choose what point you would like to know the neighbours from"))

        # Here we figure out from what point we wanna know the neighbours
        main_point: Point = point_dict[choice]
        for point in self.point_list:
            distance = main_point.distance(point)
            distance_dict.update({distance: point})

            # Keys are the distances
            # Values are the points themselves
            keys = list(distance_dict.keys())
            values = list(distance_dict.values())
            distance_dict = {}

        for key in keys:
            distance_dict.update({key: values[keys.index(key)]})

        for











    def make_graph(self):
        """
        makes use of the matplotlib library to portray
        the points it has in a graph
        :return: none
        """

        # First we import all the stuff we need
        import matplotlib.pyplot as plt

        # Then we make two lists.
        # The first one containing the X-values of the points
        # The second one containing the Y-values of the points
        for point in self.point_list:
            x_value: float = point.x_axis
            y_value: float = point.y_axis

            plt.plot(x_value, y_value, linewidth=6, marker = "o", color="b")

        plt.xlabel("x-value point")
        plt.ylabel("y-value point")
        plt.show()

    def nuke(self):
        """
        Wipes all the data in the graph has stored in it
        :returns: None
        """
        sure: str = ""

        while sure != "y" or "n":
            sure: str = input("Are you sure you want to wipe the stored data? \n There is no way to undo this action! (y/n)")
            sure = sure.lower()
        if sure == "y":
            self.point_list = []
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

        import random as rand
        for num in range(0, n):
            random_x_val: float = rand.randrange(0, 1000, 1)/10
            random_y_val: float = rand.randrange(0, 1000, 1)/10
            self.point_list.append(Point(random_x_val, random_y_val))

        return None

    def __str__(self) -> str:
        return f"graph with {len(self.point_list)} points"

    def show_neighbours(self) -> None:
        txt_message: str = ""
        for point in self.point_list:
            txt_message = txt_message + str(point)+"\n"

        print(txt_message)
        return None

    def give_point(self) -> Point:
        """
        Returns a point. There is barely any practical function to this method aside from testing.
        That also is the only reason this method exists. Do with it whatever you want
        :returns: random point stored in the graph object
        """

        returned_point = random.sample(self.point_list, 1)
        print(f"the point you get is: {returned_point}")
        return returned_point

test_graph = Graph()
print("test")
test_graph.add_random_crap(10)
print(test_graph)
test_graph.show_neighbours()
test_graph.make_graph()

point = test_graph.give_point()

# This is where it all goes wrong
# point.nearest_neighbours(1)

point.show_neighbours()

