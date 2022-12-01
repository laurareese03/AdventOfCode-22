with open('numbers.txt') as f:
  lines = f.readlines()

count = 0
maxCounts = []
for i in range(0, len(lines)):
  if lines[i] != '\n':
    count += int(lines[i])
  else:
    maxCounts.append(count)
    count = 0
maxCounts.append(count) #one final count

maxCounts.sort(reverse=True)

print(maxCounts[0] + maxCounts[1] + maxCounts[2])