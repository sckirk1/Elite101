import matplotlib.pyplot as plt
import numpy as np

anchor_x_coords = []
anchor_y_coords = []
x_coords = []
y_coords = []
number_of_iterations = 10000
number_of_anchors = int(input("Number of anchor points: "))

# This is the percent we get closer to the anchor point
# For the most part this works for n points. .5 gets weird in some cases 
jump_percent = 1 / (number_of_anchors - 1)

# Or if you want to specify it every time
# percent = float(input("Percent of jump"))


# To simplify the placement of the anchors, I just placed them along a circle
radius = 100
for i in range(number_of_anchors):
    angle = (2.0 * np.pi) * (i / number_of_anchors)
    anchor_x_coords.append(radius * np.cos(angle))
    anchor_y_coords.append(radius * np.sin(angle))

# Same with the starting point, I just put it somewhere randomly on a circle
starting_point_angle = (2.0 * np.pi) * np.random.rand()
starting_point_x = radius * np.cos(starting_point_angle)
starting_point_y = radius * np.sin(starting_point_angle)

first_go = np.random.randint(0, number_of_anchors)
x_coords.append(jump_percent * (anchor_x_coords[first_go] + starting_point_x))
y_coords.append(jump_percent * (anchor_y_coords[first_go] + starting_point_y))
for n in range(number_of_iterations):
    anchor_num = np.random.randint(0, number_of_anchors)

    # This isn't a perfect way to go a percent amount closer, but it works for going halfway, so I'll leave it
    x_coords.append(jump_percent * (anchor_x_coords[anchor_num] + x_coords[len(x_coords) - 1]))
    y_coords.append(jump_percent * (anchor_y_coords[anchor_num] + y_coords[len(y_coords) - 1]))

    # This also isn't a good way to do it. We need the absolute difference between the points, and then we should add
    # the product of that and the percent to the point that is farther left (or down)
    # But it makes fun pictures, so it doesn't matter

    # point_x_coordinates.append(anchor_x_coordinates[anchor_num] + percent_of_jump * (
    # anchor_x_coordinates[anchor_num] - point_x_coordinates[len(point_x_coordinates) - 1]))
    # point_y_coordinates.append(anchor_y_coordinates[anchor_num] + percent_of_jump * (anchor_y_coordinates[
    # anchor_num] - point_y_coordinates[len(point_y_coordinates) - 1]))

plt.scatter(x_coords, y_coords, c='red', s=1)
plt.scatter(anchor_x_coords, anchor_y_coords, c="blue")
plt.scatter(starting_point_x, starting_point_y, c="green")
plt.show()
