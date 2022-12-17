This file is for my own experiments
I am going to try to build my very own machine learning algorithms from the ground up, and see how far I can get
I try to keep the usage of libraries to a minimum cuz I hate them :(

the "points and KNN"-file contains the point class with its methods which works perfectly fine.
However, the next big challenge will be creating many instances of the point class
while making sure all points stay connected in the network.
I think the best way to approach this is by creating a Graph class which forces
the existing points to connect with the new point once a new one gets instantiated

Having a the ability to visually portray a graph is nice, so I decided to dip my toes into the water
with matplotlib library which had to be downloaded using pip.
for this I ran the following commands in the terminal:

py -m pip install -U pip
-------------------------------
py -m pip install -U matplotlib

Now I should be able to import matplotlib like my other files.
I hope I wont have to download the stuff each time I'm gonna use the library.
But I guess we'll see

Status Update 1: It does let itself get imported like my other files

What also is pretty neat is that there is a lot of stuff available to mess around with.
Here are a couple of examples:
-https://github.com/matplotlib/matplotlib/blob/main/examples/animation/dynamic_image.py
-https://www.geeksforgeeks.org/matplotlib-tutorial/#getting%20started
-https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py