import random
import numpy


# import pyglet
# from pyglet import shapes

# GAME_HEIGHT = 100
# GAME_WIDTH = 100
# batch = pyglet.graphics.Batch()
# window = pyglet.window.Window(GAME_HEIGHT, GAME_WIDTH)


class Node:
    def __init__(self, coordinates, height, width):
        self.height = height
        self.width = width
        self.coordinates = coordinates

    def get_neighbors(self):
        neighbors = []
        if self.width <= 0 or self.height <= 0:
            print("Invalid dimensions")
            return
        if self.coordinates[0] + 1 < self.height:
            cord = (self.coordinates[0] + 1, self.coordinates[1])
            neighbors.append(cord)
            print(cord)
        if self.coordinates[0] - 1 >= 0:
            cord = (self.coordinates[0] - 1, self.coordinates[1])
            neighbors.append(cord)
            print(cord)
        if self.coordinates[1] + 1 < self.width:
            cord = (self.coordinates[0], self.coordinates[1] + 1)
            neighbors.append(cord)
            print(cord)
        if self.coordinates[1] - 1 >= 0:
            cord = (self.coordinates[0], self.coordinates[1] - 1)
            neighbors.append(cord)
            print(cord)
        return neighbors

    def get_edges(self):
        node_neighbors = self.get_neighbors()

if __name__ == '__main__':
    cord = (1, 1)
    node = Node(cord, 2, 2)
    neighbors = node.get_neighbors()
    print(neighbors)