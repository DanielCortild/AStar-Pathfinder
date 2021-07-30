#!/usr/bin/env python
# encoding: utf-8
"""
node.py - Node Class of every node (square) on grid (screen)
~ Daniel Cortild, 30 July 2021
"""

import pygame
from constants import *

class Node:
  """ Node Class, represents each node (square) on the grid (screen) """
  def __init__(self, row, col, width, total_rows):
    """ Initializes Node instance
    Params
      row: The index of the row of the node (Int)
      col: The index of the col of the node (Int)
      width: The width of every node (Int)
      total_rows: Total number of rows (Int)
    """
    self.row = row
    self.col = col
    self.width = width
    self.x = row * width
    self.y = col * width
    self.color = WHITE
    self.neighbours = []
    self.total_rows = total_rows

  def get_pos(self):
    """ Get position of the node in terms of rows and columns """
    return self.row, self.col
  
  def is_barrier(self):
    """ Get whether the given node is a barrier (Black square) or not """
    return self.color == BLACK

  def reset(self):
    """ Reset status of the node (Return to white/unused state) """
    self.color = WHITE

  def make_closed(self):
    """ Make the node closed (Already visited and disregarded) """
    self.color = RED

  def make_open(self):
    """ Make the node open (Added to list of future considerations) """
    self.color = GREEN
  
  def make_barrier(self):
    """ Make the node a barrier (The path may not cross such a node) """
    self.color = BLACK

  def make_start(self):
    """ Indicate the start point of our wanted path """
    self.color = ORANGE

  def make_end(self):
    """ Indicate the end point of our wanted path """
    self.color = TURQUOISE

  def make_path(self):
    """ Indicate our wanted path """
    self.color = PURPLE

  def draw(self, win):
    """ Draws the node on the window
    Params
      win: The window to draw on (PyGame window object)
    """
    pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

  def update_neighbours(self, grid):
    """ Update the list of neighbours which are not barriers
    Params
      grid: The entire grid of nodes (Grid of Node objects)
    """
    self.neighbours = []
    neighbours = [(1, 0), (0,1), (-1, 0), (0, -1)]
    for neighbour in neighbours:
      if 0 <= self.row + neighbour[0] < self.total_rows and \
            0 <= self.col + neighbour[1] < self.total_rows:
        neighbour_node = grid[self.row + neighbour[0]][self.col + neighbour[1]]
        if not neighbour_node.is_barrier():
          self.neighbours.append(neighbour_node)

  def __lt__(self, other):
    """ Compares two Nodes (Only present for completeness in the PriorityQueue)
    Params:
      other: The second Node to compare
    """
    return False