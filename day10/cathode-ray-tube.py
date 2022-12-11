with open('program.txt') as f:
  lines = f.readlines()

count = 1
cycle = 1
signalSum = 0

def get_signal_strength(count, cycle):
  return count * cycle

for line in lines:
  line = line.strip()

  if line == 'noop':
    if ((cycle + 20) % 40 == 0 and cycle < 230):
      signalSum += get_signal_strength(count, cycle)
    cycle += 1
  
  else:
    line = line.split(' ')
    if ((cycle + 20) % 40 == 0 and cycle < 230):
      signalSum += get_signal_strength(count, cycle)
    cycle += 1
    if ((cycle + 20) % 40 == 0 and cycle < 230):
      signalSum += get_signal_strength(count, cycle)
    cycle += 1
    count += int(line[1])

print(signalSum)