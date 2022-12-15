import numpy as np

with open('scans.txt') as f:
  lines = f.readlines()

def fall_sand(point):
  try:
    global grid
    if grid[point[0]+1][point[1]] == '.':
      print('fall!')
      return fall_sand((point[0]+1, point[1]))
    else:
      print('bottom blocked')
      if grid[point[0]+1][point[1]-1] == '.':
        print('left fall!')
        return fall_sand((point[0]+1, point[1]-1))
      elif (grid[point[0]+1][point[1]+1] == '.'):
        print('right fall!')
        return fall_sand((point[0]+1, point[1]+1))
      else:
        print('blocked!')
        grid[point[0]][point[1]] = 'o'
        return True
  except:
    print('infinite fall!')
    return False

width = [1000, -1]
height = [1000, -1]
for i in range(0, len(lines)):
  lines[i]  = lines[i].strip().split(' -> ')
  for j in range(0, len(lines[i])):
    lines[i][j] = point = lines[i][j].split(',')
    width = [min(width[0], int(point[0])), max(width[1], int(point[0]))]
    height = [min(height[0], int(point[1])), max(height[1], int(point[1]))]

grid = np.full((height[1]+1, width[1]-width[0]+1), '.')
for line in lines:
  for i in range(0, len(line)-1):
    xmin = min(int(line[i][1]), int(line[i+1][1]))
    xmax = max(int(line[i][1]), int(line[i+1][1])) + 1
    ymin = min(int(line[i+1][0])-width[0], int(line[i][0])-width[0])
    ymax = max(int(line[i+1][0])-width[0], int(line[i][0])-width[0]) + 1
    grid[xmin:xmax, ymin:ymax] = '#'

grid = grid.tolist()
for line in grid:
  print(line)
startIndex = 500
trueStart = startIndex-width[0]
print(trueStart)

falling = True
count = 0 
while falling:
  count += 1
  falling = fall_sand((0, trueStart))
print(count-1)