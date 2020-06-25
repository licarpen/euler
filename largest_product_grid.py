import numpy as np
from operator import mul
import functools

grid = np.genfromtxt('data/largest_product_grid.txt', delimiter=' ')

def find_largest_product(txt_file, delimiter):
  grid = np.genfromtxt(txt_file, delimiter=delimiter)
  products = []
  for i in range(20):
    for j in range(20):
      if j + 3 < 20:
        products.append(functools.reduce(mul, [grid[i][j + x] for x in range(4)]))
      if i + 3 < 20:
        products.append(functools.reduce(mul, [grid[i + y][j] for y in range(4)]))
      if i + 3 < 20 and j + 3 < 20:
        products.append(functools.reduce(mul, [grid[i + x][j + x] for x in range(4)]))
      if i + 3 < 20 and j > 2:
        products.append(functools.reduce(mul, [grid[i + x][j - x] for x in range(4)]))
  return max(products)

find_largest_product('data/largest_product_grid.txt', ' ')