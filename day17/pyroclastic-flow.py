with open('wind-gusts.txt') as f:
  lines = f.readlines()
  wind = lines[0].strip()

shapes = [['####'], ['.#.','###','.#.'], ['###','..#','..#'], ['#','#','#','#'], ['##','##']]
arena = ['#######']
windIndex = 0

def get_clashing_pieces(direction, leftIndex, shape, arenaLine):
  clashing = False
  for k in range(len(shape)):
    arenaHash = [n for n in range(len(arena[arenaLine + k])) if arena[arenaLine+k].find('#', n) == n]
    shapeHashPlus = [(n+leftIndex+1) for n in range(len(shape[k])) if shape[k].find('#', n) == n]
    shapeHashMinus = [(n+leftIndex-1) for n in range(len(shape[k])) if shape[k].find('#', n) == n]
    if direction == '>':
      clashing = clashing or len(set(shapeHashPlus).intersection(set(arenaHash))) != 0 # right
    else:
      clashing = clashing or len(set(shapeHashMinus).intersection(set(arenaHash))) != 0 # right
  return clashing

def get_left_index(direction, leftIndex, shape, arenaLine):
  piecesClash = get_clashing_pieces(direction, leftIndex, shape, arenaLine)
  if direction == '>':
    if leftIndex + len(shape[0]) < 7 and not piecesClash:
      leftIndex +=1
  else:
    if leftIndex != 0 and not piecesClash:
      leftIndex -=1
  return leftIndex

def get_ground_clash(arenaIndex, shape, leftIndex):
  for l in range(len(shape)):
    gameHash = [n for n in range(len(arena[arenaIndex+l])) if arena[arenaIndex+l].find('#', n) == n]
    text = '.......'
    text = text[:leftIndex] + shape[l] + text[leftIndex+len(shape[l]):]
    shapeHash = [n for n in range(len(text)) if text.find('#', n) == n]
    if len(set(gameHash).intersection(set(shapeHash))) != 0:
      return True

def fall(shape):
  global windIndex, arena
  arena += ['.......'] * 3 # extra height
  leftIndex = 2
  settled = False
  arenaIndex = len(arena) - 1
  arena += ['.......'] * 4 # for shape comparison

  while not settled:
    #handle windblow
    direction = wind[windIndex]
    windIndex = (1+windIndex)%len(wind)

    leftIndex = get_left_index(direction, leftIndex, shape, arenaIndex + 1)
    #handle settle condition
    if get_ground_clash(arenaIndex, shape, leftIndex):
      for i in range(len(shape)):
        text = arena[arenaIndex + 1 + i]
        poses = [(n+leftIndex) for n in range(len(shape[i])) if shape[i].find('#', n) == n]
        text = list(text)
        for pos in poses:
          text[pos] = '#'
        text = ''.join(text)
        arena[arenaIndex + 1 + i] = text
      for j in range(len(arena)-1, len(arena)-11, -1):
        if arena[-1] == '.......':
          del arena[-1]
      settled = True
    else:
      arenaIndex -= 1
f = open("demofile2.txt", "a")
for rock in range(1000000000000):
  if windIndex != 0 and rock % (windIndex*len(shapes)) == 0:
    print(len(arena)-1, rock)
  fall(shapes[rock%5])
  f.write(str(len(arena)-1) + '\n')
f.close()

# for i in range(len(arena)-1, -1, -1):
#   print(arena[i])

print(len(arena)-1)