import re, time as t

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
# will track pressure over time
maxv = 0
def get_path(start, time, releasedPressure):
  global maxv
  print("START", releasedPressure, start, time)
  if time <= 0:
    return releasedPressure
  frontier = [[tunnels[start], 0, 0]]
  visited = {}
  while len(frontier) != 0:
    valve = frontier.pop(0)
    for connection in valve[0]['connections']:
      if connection not in visited.keys():
        frontier.append([tunnels[connection], valve[1]+1])
        visited[connection] = ((time-(valve[1]+2))*tunnels[connection]['pressure'])

  visited = {k: v for k, v in sorted(visited.items(), key=lambda item: item[1], reverse=True)}
  for visit in visited.keys(): 
    if visited[visit] == 0:
      return releasedPressure
    if not tunnels[visit]['isOpen']:
      tunnels[visit]['isOpen'] = True
      timeDist = time - (visited[visit]/tunnels[visit]['pressure'])
      value = get_path(visit, time - int(timeDist), releasedPressure + visited[visit])
      maxv = max(maxv, int(value or 0))
      tunnels[visit]['isOpen'] = False

get_path('AA', 30, 0)
print("HERE", maxv)

# def get_next_move():
  # 2 kinds of return values
  # if next decision is move, return 0
  # else next decision is open current valve, return pressure of valve
