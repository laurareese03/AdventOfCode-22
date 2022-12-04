with open('rucksacks.txt') as f:
  lines = f.readlines()

for line in lines:
  line.strip()

def convert_to_value(letter):
  if letter.isupper():
    return ord(letter)-64+26
  else:
    return ord(letter)-96

def part_a():
  score = 0
  for line in lines:
    line = line.strip()

    bags = [line[0:int(len(line)/2)], line[int(len(line)/2):len(line)]]
    res = set(bags[0]).intersection(bags[1])

    for letter in res:
      score += convert_to_value(letter)
  print(score)

def part_b():
  score = 0
  for i in range(0,len(lines),3):
    res = set(lines[i].strip()).intersection(lines[i+1].strip()).intersection(lines[i+2].strip())

    for letter in res:
      score += convert_to_value(letter)
  print(score)

part_a()
part_b()