with open('program.txt') as f:
  lines = f.readlines()

count = 1
cycle = 1
crtRow = ''
crtRows = []

def get_signal_strength(count, cycle):
  return count * cycle

for line in lines:
  line = line.strip()

  if line == 'noop':
    if ((cycle-1) % 40 == 0):
      crtRows.append(crtRow)
      crtRow = ''
    if (count == len(crtRow) or count+1 == len(crtRow) or count-1 == len(crtRow)):
      crtRow += '#'
    else:
      crtRow += '.'
    cycle += 1
  
  else:
    line = line.split(' ')
    if ((cycle-1) % 40 == 0):
      crtRows.append(crtRow)
      crtRow = ''
    if (count == len(crtRow) or count+1 == len(crtRow) or count-1 == len(crtRow)):
      crtRow += '#'
    else:
      crtRow += '.'
    cycle += 1
    if ((cycle-1) % 40 == 0):
      crtRows.append(crtRow)
      crtRow = ''

    if (count == len(crtRow) or count+1 == len(crtRow) or count-1 == len(crtRow)):
      crtRow += '#'
    else:
      crtRow += '.'
    cycle += 1
    count += int(line[1])

  print(crtRow)

crtRows.append(crtRow)

for row in crtRows:
  print(row)
