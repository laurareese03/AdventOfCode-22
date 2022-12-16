import re

with open('sensors.txt') as f:
  lines = f.readlines()

testLine = 2000000

def manhattan_distance(sensor, beacon):
  return abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

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
  print(sensor, 'Here')
  if abs(testLine - sensor[0][1]) < sensor[1]:
    for i in range(sensor[0][0], (sensor[0][0] + abs(sensor[1] - abs(sensor[0][1] - testLine))+1)):
      rangedSensor.add(i)
    for i in range(sensor[0][0], sensor[0][0] - abs(sensor[1] - abs(sensor[0][1] - testLine))-1, -1):
      rangedSensor.add(i)

for beacon in beacons:
  rangedSensor.remove(beacon)

print(len(rangedSensor))