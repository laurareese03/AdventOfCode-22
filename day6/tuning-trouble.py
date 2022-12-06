with open('datastreams.txt') as f:
  lines = f.readlines()

# changes between part a and b
UNIQUE_STRING_LENGTH = 14

for line in lines:
  for char in range(0, len(line)-(UNIQUE_STRING_LENGTH-1)):
    if len(set([*line[char:char+UNIQUE_STRING_LENGTH]])) == UNIQUE_STRING_LENGTH:
      print(char+UNIQUE_STRING_LENGTH)
      break