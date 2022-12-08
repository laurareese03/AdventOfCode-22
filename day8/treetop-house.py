import numpy as np

with open('tree-grid.txt') as f:
  lines = f.readlines()

arr = []
for line in lines:
  arr.append(list(line.strip()))

trees = np.array(arr)
visible = np.zeros(trees.shape)

def get_lr_columns():
  for row in range(0, len(trees)):
    for column in range(0, len(trees[row])):
      if (all(x < trees[row][column] for x in trees[row][:column])):
        visible[row][column] = 1

def part_a():
  global trees
  global visible
  get_lr_columns()
  trees = np.fliplr(trees)
  visible = np.fliplr(visible)
  get_lr_columns()
  trees = trees.transpose()
  visible = visible.transpose()
  get_lr_columns()
  trees = np.fliplr(trees)
  visible = np.fliplr(visible)
  get_lr_columns()

  print(np.sum(visible))

def get_tree_distance(array, height):
  for i in range(0, len(array)):
    if not (all(x < height for x in array[:i])):
      return i
  return len(array)

def get_tree_score(row, column):
  global trees
  height = trees[row, column]
  score = (
    get_tree_distance(np.flipud(trees[row][:column]), height) *
    get_tree_distance(trees[row][column+1:], height) *
    get_tree_distance(trees[row+1:,column], height) *
    get_tree_distance(np.flipud(trees[:row,column]), height) 
  )
  return score

def part_b():
  maxTreeScore = 0
  for row in range(0, len(trees)):
    for column in range(0, len(trees[row])):
      treeScore = get_tree_score(row, column)
      maxTreeScore = max(maxTreeScore, treeScore)

  print(maxTreeScore)

part_a()
part_b()