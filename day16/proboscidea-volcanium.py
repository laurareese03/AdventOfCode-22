import re

with open('valves.txt') as f:
  lines = f.readlines()

# File reading
tunnels = {}
for line in lines:
  line = line.strip()
  # parse lines in the form [(valve), (flow rate), (...connected tunnels)]
  result = [d for d in re.findall(r'-?\d+|[A-Z]{2}', line)]

  tunnels[result[0]] = {
    'pressure': int(result[1]),
    'connections': result[2:],
    'isOpen': False
  }

# pressure tracking and decision making
builtPressure = 0 # for opened valves
releasedPressure = 0 # will track pressure over time

arr = []
frontier = [[tunnels['AA'], 0, 0]]
visited = {}
while len(frontier) != 0:
  valve = frontier.pop(0)
  for connection in valve[0]['connections']:
    if connection not in visited.keys():
      frontier.append([tunnels[connection], valve[1]+1])
      visited[connection] = ((30-(valve[1]+1))*tunnels[connection]['pressure'])

print(visited)




# def get_next_move():
  # 2 kinds of return values
  # if next decision is move, return 0
  # else next decision is open current valve, return pressure of valve




# time simulation
for i in range(0, 30): # time limit
  releasedPressure += builtPressure
# find_best_route('AA')
  # builtPressure = get_next_move()