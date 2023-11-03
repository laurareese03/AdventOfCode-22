with open('data_reads.txt') as f:
  drops = f.readlines()

droplets = []
# convert to tuples
for drop in drops:
  droplet = tuple(int(i) for i in drop.strip().split(','))
  droplets.append(droplet)

# cubes are adjacent if 2/3 numbers in the tuple are the same, and if 1/3 is 1 away
# use zip to to find the index difference between the tuples. 
# absolute value of the sums should equal 1. index difference should only contain 0 or 1
def are_adjacent_cubes(c_one, c_two):
  return (abs(sum([a-b for a,b in zip(c_one, c_two)])) == 1 and 
    (set([a-b for a,b in zip(c_one, c_two)]) == {0, 1} or set([a-b for a,b in zip(c_one, c_two)]) == {0, -1})) 
  

count = 0
# logic here -> (# of cubes) * 6 - (# of adjacent pairs * 2)
# will this work? who's to say
for i in range(len(droplets)-1):
  for j in range(i+1, len(droplets)):
    if are_adjacent_cubes(droplets[i], droplets[j]):
      count +=1

print(count)
print(len(droplets) * 6 - (count * 2))