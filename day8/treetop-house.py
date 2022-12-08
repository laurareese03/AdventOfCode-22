import numpy as np

with open('tree-grid.txt') as f:
  lines = f.readlines()

arr = []
for line in lines:
  arr.append(list(line.strip()))

trees = np.array(arr)
visible = np.zeros(trees.shape)

def get_lr_columns():
  # idea - search from left to right, then transpose matrix and search from left to right again.
  for row in range(0, len(trees)):
    for column in range(0, len(trees[row])):
      if (all(x < trees[row][column] for x in trees[row][:column])):
        visible[row][column] = 1

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