#!/usr/bin/env python
# encoding: utf-8
"""
aStarAlgorithm.py - Executes the A* Pathfinder Algorithm
~ Daniel Cortild, 30 July 2021
"""

import pygame
from queue import PriorityQueue

def heuristic(point1, point2):
  """ Return the value of the heuristic between point1 and point2
  Params
    point1: First point to consider (Node object)
    point2: Second point to consider (Node object)
  Returns
    h: Value of the heuristic (Float)
  """
  x1, y1 = point1.get_pos()
  x2, y2 = point2.get_pos()
  # h = 0 # Dijkstra Algorithm
  h = abs(x1 - x2) + abs(y1 - y2) # Manhatten Distance
  # h = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # Euclidian Distance
  return h

def construct_path(parents, end, draw):
  """ Constructs the path between the endpoint and the startpoint
  Params:
    parents: Dictionary of parents of each considered node (Dictionary of Node: Node)
    end: End node (Node object)
    draw: Function drawing the window (Function)
  """
  while end in parents.keys():
    end = parents[end]
    end.make_path()
    draw()
    
def a_star_algorithm(draw, grid, start, end):
  """ Executes the A* Algorithm to find shortest path between startpoint and endpoint in the grid
  Params
    draw: Function drawing the window (Function)
    grid: Grid of nodes building the window (Grid of Node objects)
    start: Start point (Node object)
    end: End point (Node object)
  """
  count = 0
  open_set = PriorityQueue()
  open_set.put((0, count, start))
  parent = {}
  score = {node: float("inf") for row in grid for node in row}
  score[start] = 0

  open_set_hash = { start }

  while not open_set.empty():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    
    current = open_set.get()[2]
    open_set_hash.remove(current)

    if current == end:
      construct_path(parent, end, draw)
      start.make_start()
      end.make_end()
      return

    for neighbour in current.neighbours:
      temp_score = score[current] + 1

      if temp_score < score[neighbour]:
        parent[neighbour] = current
        score[neighbour] = temp_score

        if neighbour not in open_set_hash:
          count += 1
          f_score = temp_score + heuristic(neighbour, end)
          open_set.put((f_score, count, neighbour))
          open_set_hash.add(neighbour)
          neighbour.make_open()

    draw()

    if current != start:
      current.make_closed()