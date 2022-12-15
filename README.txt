This file is for my own experiments
I am going to try to build my very own machine learning algorithms from the ground up, and see how far I can get
I try to keep the usage of libraries to a minimum cuz I hate them :(

the "points and KNN"-file contains the point class with its methods which works perfectly fine.
However, the next big challenge will be creating many instances of the point class
while making sure all points stay connected in the network.
I think the best way to approach this is by creating a Graph class which forces
the existing points to connect with the new point once a new one gets instantiated