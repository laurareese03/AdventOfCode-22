with open('assignments.txt') as f:
  lines = f.readlines()

def get_rooming_lists(line):
  rooms = []
  pair = []
  assignments = line.strip().split(',')
  for assignment in assignments:
    rooms = assignment.split('-')
    pair.append(set(range(int(rooms[0]), int(rooms[1])+1)))

  return pair

def part_a():
  count = 0

  for line in lines:
    pair = get_rooming_lists(line)

    if (pair[0].intersection(pair[1]) == pair[0]) or pair[1].intersection(pair[0]) == pair[1]:
      count += 1

  print(count)

def part_b():
  count = 0
  for line in lines: 
    pair = get_rooming_lists(line)

    if (len(pair[0].intersection(pair[1])) > 0):
      count += 1

  print(count)

part_a()
part_b()