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

        # Here we present the user with the choices he has, and allow him to pick one
        choice_dict: dict = {}
        point_counter: int = 1
        for point in self.point_list:
            print(F"[{point_counter}] {point}")
            point_counter+=1
            choice_dict.update({point_counter: point})

        choice: int = 0
        choice: int = int(input("Please select your point"))
        while choice not in range(1, point_counter+1):
            print(f"Your choice has to be between 1 and {point_counter}")
            print(f"Your value: {choice} did not fall within that range")
            choice: int = int(input("Please try again"))

        chosen_point: Point = choice_dict[int(choice+1)]
        # print(chosen_point)

        # Now we know which from which point the user wants the nearest neighbours,
        # we simply calculate the distances and store it in a dictionary

        distance_point_dict: dict = {}
        print(chosen_point)

        for point in self.point_list:
            if point == chosen_point:
                # print(f"skipped point: {point}")
                continue
            else:
                distance: float = chosen_point.distance(point)
                distance_point_dict.update({distance: point})

        # Now we just take the n-amount of shortest distances and give them back
        distance_list = list(distance_point_dict.keys())
        distance_list.sort()

        print("test test")
        print("The closest neighbours are:")
        distances_counter: int = 0
        for shortest_distances in distance_list:
            if distances_counter == n_neighbours:
                break
            else:

                print(f"point: {distance_point_dict[shortest_distances]} at {shortest_distances} away")

                distances_counter += 1

        # All there is left is choosing what to return

        return None

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
test_graph.closest_neighbours(2)



