with open('games.txt') as f:
  lines = f.readlines()

def determineWinner(opp, player):
  if (opp - player) % 3 == 2:
    return 6 # win
  if opp == player:
    return 3 # draw
  if (opp - player) % 3 == 1:
    return 0 # loss

def determinePlay(opp, player):
  retVal = -1
  if player == 3:
    retVal = (opp - 2) % 3 # win
  if player == 2:
    retVal = opp # draw
  if player == 1:
    retVal = (opp - 1) % 3 # loss

  if retVal == 0:
    return 3
  else:
    return retVal

def convertToInt(line):
  returnArray = []
  for letter in line:
    if letter == 'A' or letter == 'X':
      returnArray.append(1)
    if letter == 'B' or letter == 'Y':
      returnArray.append(2)
    if letter == 'C' or letter == 'Z':
      returnArray.append(3)
  return returnArray

def partA():
  score = 0
  for line in lines:
    lineScore = 0
    hold = convertToInt(line.strip().split(' '))
    lineScore += hold[1]
    lineScore += determineWinner(hold[0], hold[1])
    score += lineScore

  print(score)

def partB():
  score = 0
  for line in lines:
    lineScore = 0
    hold = convertToInt(line)
    lineScore += (hold[1]-1)*3
    lineScore += determinePlay(hold[0], hold[1])

    print((hold[1]-1)*3, determinePlay(hold[0], hold[1]))
    score += lineScore

  print(score)

partA()
partB()