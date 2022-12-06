with open('stacks.txt') as f:
  lines = f.readlines()

instructions = []
stacks = []

class Stack:
  def __init__(self, name, boxes):
    self.name = name
    self.boxes = boxes

# find the line break to separate instructions from the stacks
index = lines.index('\n')
instructions = lines[index+1:len(lines)]
boxes = lines[0:index-1]
stacks = lines[index-1].strip().split(' ')

# get the objects set for 
stacks = [item for item in stacks if '' != item]
stackList = []
print(len(boxes), len(stacks))
print(boxes)

for stack in stacks:
  hold = Stack(stack, [])
  stackList.append(hold)

for i in range(len(boxes), 0, -1):
  for letterIndex in range(2, len(boxes[i-1]), 4):
    if(boxes[i-1][letterIndex-1] != ' '):
      stackList[int((letterIndex-2)/4)].boxes.append(boxes[i-1][letterIndex-1])

for stack in stackList:
  print(stack.boxes)

for instruction in instructions:
  print(instruction)
  location = instruction.index('move ')+5
  count = instruction[location:location+2].strip()
  fromName = int(instruction.index('from ')+5)
  toName = int(instruction.index('to ')+3)
  for move in range(0, int(count)):
    fromIndex = instruction[int(fromName):int(fromName+1)]
    hold = stackList[int(fromIndex)-1].boxes.pop()
    toIndex = instruction[int(toName):int(toName+1)]
    stackList[int(toIndex)-1].boxes.append(hold)

  for stack in stackList:
    print(stack.boxes)