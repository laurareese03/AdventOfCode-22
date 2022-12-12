import numpy as np

with open('hill-map.txt') as f:
  hill = f.readlines()

arr = []
for geo in hill:
  arr.append(list(geo.strip()))

hill = np.array(arr)
start = np.where(hill == 'S')
start = (start[0][0], start[1][0])
end = np.where(hill == 'E')
end = (end[0][0], end[1][0])
hill[end] = 'z'

# Breadth First Search baybee
frontier = [[start, 0]]
frontierButWorse = [start]
visited = []
height = ord('a')

while len(frontier) != 0:
  place = frontier.pop()
  if place[0] == end:
    print(place)
    break
  if hill[tuple(place[0])] != 'S':
    height = ord(hill[place[0]])
  visited.append(place[0])
  
  if place[0][0] + 1 < len(hill) and ord(hill[place[0][0]+1, place[0][1]]) <= (height + 1) and (place[0][0]+1, place[0][1]) not in visited and (place[0][0]+1, place[0][1]) not in frontierButWorse:
    frontier.insert(0, [(place[0][0]+1, place[0][1]), place[1]+1])
    frontierButWorse.append((place[0][0]+1, place[0][1]))
  if place[0][1] + 1 < len(hill[place[0][0]]) and ord(hill[place[0][0], place[0][1]+1]) <= (height + 1) and (place[0][0], place[0][1]+1) not in visited and (place[0][0], place[0][1]+1) not in frontierButWorse:
    frontier.insert(0, [(place[0][0], place[0][1]+1), place[1]+1])
    frontierButWorse.append((place[0][0], place[0][1]+1))
  if place[0][0] - 1 >= 0 and ord(hill[place[0][0]-1, place[0][1]]) <= (height + 1) and (place[0][0]-1, place[0][1]) not in visited and (place[0][0]-1, place[0][1]) not in frontierButWorse:
    frontier.insert(0, [(place[0][0]-1, place[0][1]), place[1]+1])
    frontierButWorse.append((place[0][0]-1, place[0][1]))
  if place[0][1] - 1 >= 0 and ord(hill[place[0][0], place[0][1]-1]) <= (height + 1) and (place[0][0], place[0][1]-1) not in visited and (place[0][0], place[0][1]-1) not in frontierButWorse:
    frontier.insert(0, [(place[0][0], place[0][1]-1), place[1]+1])
    frontierButWorse.append((place[0][0], place[0][1]-1))