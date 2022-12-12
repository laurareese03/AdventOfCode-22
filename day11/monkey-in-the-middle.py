with open('observations.txt') as f:
  observations = f.readlines()

monkeyDeets = []
monkeyDeet = ''

for observation in observations:
  if observation != '\n':
    monkeyDeet += observation
  else:
    monkeyDeets.append(monkeyDeet)
    monkeyDeet = ''
monkeyDeets.append(monkeyDeet)

use = []
for monkeyDeet in monkeyDeets:
  hold = []
  monkeyDeet = monkeyDeet.split('\n')
  hold.append(monkeyDeet[1][18:].split(', '))
  hold.append(monkeyDeet[2][19:])
  hold.append(monkeyDeet[3][21:])
  hold.append(monkeyDeet[4][29:])
  hold.append(monkeyDeet[5][30:])
  use.append(hold)

interactions = [0]*len(use)

stressModifier = 1
for monkey in use:
  stressModifier *= int(monkey[2])

for j in range(0, 10000): # handle each round
  for i in range(0, len(use)):
    for old in use[i][0].copy():
      new = eval(use[i][1], {"old": int(old)})  # inspect operation
      if new % int(use[i][2]) == 0:             # test case
        use[int(use[i][3])][0].append(new % stressModifier)  # outcomes
      else:
        use[int(use[i][4])][0].append(new % stressModifier)
      use[i][0].remove(old) 
      interactions[i] += 1
  print(j)

interactions.sort(reverse=True)
print(interactions[0]*interactions[1])