#!/usr/bin/env python
# encoding: utf-8
"""
main.py - Main script for the A* Pathfinder Algorithm
~ Daniel Cortild, 30 July 2021
"""

import pygame
from constants import *
from node import Node
from aStarAlgorithm import *

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinder Algorithm Visualization")

def make_grid(rows, width):
  """ Create grid of nodes
  Params
    rows: Number of rows (Int)
    width: Width of entire screen (Int)
  Returns
    grid: Grid of nodes (2D array of Node objects)
  """
  gap = width // rows
  grid = []
  for i in range(rows):
    grid.append([])
    for j in range(rows):
      node = Node(i, j, gap, rows)
      grid[i].append(node)
  return grid

def draw_grid(win, rows, width):
  """ Draw the grid on the window
  Params
    win: Window to draw on (PyGame Window object)
    rows: Number of rows (Int)
    width: Width of screen (Int)
  """
  gap = width // rows
  for i in range(rows):
    pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))

def draw(win, grid, rows, width):
  """ Draws the nodes on the screen
  Params
    win: Window to draw on (PyGame Window object)
    grid: Grid of nodes to draw (2D array of Node objects)
    rows: Number of rows (Int)
    width: Width of screen (Int)
  """
  win.fill(WHITE)
  for row in grid:
    for node in row:
      node.draw(win)
  draw_grid(win, rows, width)
  pygame.display.update()
  
def get_clicked_pos(pos, rows, width):
  """ Get the row and column at a certain position
  Params
    pos: Position (Pair of ints)
    rows: Number of rows (Int)
    width: Width of screen (Int)
  Returns
    row: Row at the position
    col: Column at the position
  """
  gap = width // rows
  x, y = pos

  row = x // gap
  col = y // gap

  return row, col

def main(win, rows, width):
  """ Main function, run the entire algorithm
  Params
    win: Window to draw on (PyGame Window object)
    rows: Number of rows (Int)
    width: Width of screen (Int)
  """
  grid = make_grid(rows, width)

  start = None
  end = None

  run = True
  started = False

  while run:
    draw(win, grid, rows, width)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_c:
          started = False
          start = None
          end = None
          grid = make_grid(rows, width)

      if started:
        continue

      if pygame.mouse.get_pressed()[0]: # Left Mouse Button
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        node = grid[row][col]
        if not start and node != end:
          start = node
          start.make_start()
        elif not end and node != start:
          end = node
          end.make_end()
        elif node != end and node != start:
          node.make_barrier()

      elif pygame.mouse.get_pressed()[2]: # Right Mouse Button
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        node = grid[row][col]
        node.reset()
        if node == start:
          start = None
        if node == end:
          end = None

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and start and end:
          started = True
          for row in grid:
            for node in row:
              node.update_neighbours(grid)
          a_star_algorithm(lambda: draw(win, grid, rows, width), grid, start, end)
  
  pygame.quit()

if __name__ == "__main__":
  main(win, ROWS, WIDTH)