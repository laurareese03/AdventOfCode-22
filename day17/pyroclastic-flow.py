with open('wind-gusts.txt') as f:
  lines = f.readlines()
  wind = lines[0]

shapes = [['####'], ['.#.','###','.#.'], ['###','..#','..#'], ['#','#','#','#'], ['##','##']]
arena = ['#######']
windIndex = 0

def get_clashing_pieces(direction, leftIndex, shape, arenaLine):
  clashing = False
  for k in range(0, len(shape)):
    try:
      arenaHash = [n for n in range(len(arena[arenaLine + k])) if arena[arenaLine+k].find('#', n) == n]
      shapeHash = [n for n in range(len(shape[k])) if shape[k].find('#', n) == n]
      if direction == '>':
        clashing = clashing or leftIndex + shapeHash[-1] + 1 in arenaHash # right
      else:
        clashing = clashing or leftIndex - shapeHash[0] - 1 in arenaHash # left
    except:
      print('blah')
  return clashing

  if direction == '>':
    leftIndex + len(shape[0]) not in arenaHash # right
  else:
    leftIndex - len(shape[0]) not in arenaHash # left

def get_left_index2(direction, leftIndex, shape, arenaLine):
  piecesClash = get_clashing_pieces(direction, leftIndex, shape, arenaLine)
  if direction == '>':
    if leftIndex + len(shape[0]) < 7 and not piecesClash:
      leftIndex +=1
  else:
    if leftIndex != 0 and not piecesClash:
      leftIndex -=1
  return leftIndex

def get_left_index(direction, leftIndex, shape):
  if direction == '>':
    if leftIndex + len(shape[0]) < 7:
      leftIndex +=1
  else:
    if leftIndex != 0:
      leftIndex -=1
  return leftIndex

def fall(shape):
  global windIndex, arena
  arena += ['.......'] * 3 # extra height
  leftIndex = 2
  settled = False
  arenaIndex = len(arena) - 1

  for x in range(0, 1):
    leftIndex = get_left_index(wind[windIndex], leftIndex, shape)
    windIndex = (windIndex+1) % 40
    arenaIndex -= 1
  while not settled:
    #handle windblow
    direction = wind[windIndex]
    windIndex = (1+windIndex)%len(wind)

    leftIndex = get_left_index2(direction, leftIndex, shape, arenaIndex + 1)
    #handle settle condition
    gameHash = [n for n in range(len(arena[arenaIndex])-1) if arena[arenaIndex].find('#', n) == n]
    text = '.......'
    text = text[:leftIndex] + shape[0] + text[leftIndex+len(shape[0]):]
    shapeHash = [n for n in range(len(text)-1) if text.find('#', n) == n]
    if len(set(gameHash).intersection(set(shapeHash))) != 0:
      for i in range(0,len(shape)):
        try:
          text = arena[arenaIndex + 1 + i]
        except:
          text = '.......'
        try:
          arena[arenaIndex + 1 + i] = (text[:leftIndex] + shape[i] + text[leftIndex+len(shape[i]):])
        except:
          arena.append(text[:leftIndex] + shape[i] + text[leftIndex+len(shape[i]):])
      for j in range(len(arena)-1, len(arena)-4, -1):
        if arena[-1] == '.......':
          del arena[-1]
      break
    else:
      arenaIndex -= 1

for rock in range(0,10):
  fall(shapes[rock%5]) 

  # for i in range(len(arena)-1, -1, -1):
  #   print(arena[i])
  # print()

print(len(arena)-1)