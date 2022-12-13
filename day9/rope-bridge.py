from numpy import sign # for ONE function :(

with open('directions.txt') as f:
  directions = f.readlines()

head = (0,0)
tail = []
for i in range(0, 9):
  tail.append((0,0))
tailVisited = []

def follow_trail(head, tail):
  tail = list(tail)
  if abs(tail[0]-head[0]) > 1 or abs(tail[1]-head[1]) > 1:
    if tail[0] == head[0]: #same row
      tail[1] += sign(head[1]-tail[1])

    elif tail[1] == head[1]: #same column
      tail[0] += sign(head[0]-tail[0])

    else: #neither
      tail[0] += sign(head[0]-tail[0])
      tail[1] += sign(head[1]-tail[1])
  tail = tuple(tail)
  return tail

def move_head(direction, steps, head, tail, trail):
  for step in range(0, int(steps)):
    if direction == 'U':
      head = [head[0]+1, head[1]]
    if direction == 'L':
      head = [head[0], head[1]-1]
    if direction == 'D':
      head = [head[0]-1, head[1]]
    if direction == 'R':
      head = [head[0], head[1]+1]
    tail[0] = follow_trail(head, tail[0])
    for position in range(0, len(tail)-1):
      tail[position+1] = follow_trail(tail[position], tail[position+1])
    trail.append(tail[-1])
  return [head, tail, trail]

trail = [(0,0)]
for instruction in directions:
  instruction = instruction.strip().split(' ')
  [head, tail, trail] = move_head(instruction[0], instruction[1], head, tail, trail)

trail = set(trail)
print(len(trail))