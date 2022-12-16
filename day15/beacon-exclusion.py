import re

with open('sensors.txt') as f:
  lines = f.readlines()

testLine = 2000000

def manhattan_distance(sensor, beacon):
  return abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

def get_past_manhattan_distance(sensor, dist):
  dist += 1
  values = []
  for i in range(0, dist+1):
    j = dist - i
    if (sensor[0]+i <=4000000 and sensor[0]-i >=0 and sensor[1]+j<=4000000 and sensor[1]-j>=0):
      values.append((sensor[0]+i, sensor[1]+j))
      values.append((sensor[0]-i, sensor[1]-j))
      values.append((sensor[0]-i, sensor[1]+j))
      values.append((sensor[0]+i, sensor[1]-j))
  return values

# thank you stack overflow
# https://stackoverflow.com/questions/42751063/python-filter-positive-and-negative-integers-from-string
sensors = []
beacons = set()
for line in lines:
  line = line.strip()
  result = [int(d) for d in re.findall(r'-?\d+', line)]
  sensor = [result[0], result[1]]
  beacon = [result[2], result[3]]
  if result[3] == testLine:
    beacons.add(result[2])
  sensors.append([sensor, manhattan_distance(sensor, beacon)])

rangedSensor = set()
for sensor in sensors:
  if abs(testLine - sensor[0][1]) <= sensor[1]:
    for i in range(sensor[0][0], (sensor[0][0] + abs(sensor[1] - abs(sensor[0][1] - testLine))+1)):
      rangedSensor.add(i)
    for i in range(sensor[0][0], sensor[0][0] - abs(sensor[1] - abs(sensor[0][1] - testLine))-1, -1):
      rangedSensor.add(i)

for beacon in beacons:
  rangedSensor.remove(beacon)

print(len(rangedSensor))

# can i get an f in the chat for this time complexity
past = set()
intersectors = set()
for sensor in sensors:
  print('dist for:', sensor)
  past = past.union(set(get_past_manhattan_distance(sensor[0], sensor[1])))

for testPoint in past:
  test = True
  for sensor in sensors:
    test = test and (manhattan_distance(sensor[0], testPoint) > sensor[1])
    if not test:
      break
  if test:
    print(testPoint, testPoint[0]*4000000+testPoint[1])