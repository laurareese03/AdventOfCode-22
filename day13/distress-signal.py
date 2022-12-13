with open('distress-signal.txt') as f:
  signals = f.readlines()

compList = []
count = 0
index = 1
sum = 0

def parse_lists(left, right):
  value = None
  
  while(len(left) != 0 and len(right) != 0):
    l = left.pop(0)
    r = right.pop(0)
    if (type(l) == int == type(r)):
      if (l < r):
        return True
      elif (r < l):
        return False

    else:
      if (type(l) != list):
        l = [l]
      if (type(r) != list):
        r = [r]

      if l != r:
        if len(l) == 0:
          return True
        if len(r) == 0:
          return False

      value = parse_lists(l.copy(), r.copy())
    
    if value != None:
      return value

  if len(left) > 0:
    return False
  elif len(right) > 0:
    return True

arr = []
for j in range(0, len(signals), 3):
  arr.append(eval(signals[j].strip()))
  arr.append(eval(signals[j+1].strip()))
  here = parse_lists(eval(signals[j].strip()), eval(signals[j+1].strip()))
  if here:
    count += 1
    sum += index
  index += 1

print(sum)

# modified bubble sort code from geeksforgeeks
def bubble_sort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
      # range(n) also work but outer loop will
      # repeat one time more than needed.
      # Last i elements are already in place
      for j in range(0, n-i-1):
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if not parse_lists(arr[j].copy(), arr[j+1].copy()):
          swapped = True
          hold = arr[j]
          arr[j] = arr[j + 1]
          arr[j + 1] = hold
      if not swapped:
        # if we haven't needed to make a single swap, we
        # can just exit the main loop.
        return

bubble_sort(arr)

twoPos = 0
sixPos = 0
for i in range(0, len(arr)):
  if parse_lists([[2]], arr[i].copy()):
    twoPos = i+1
    break
for i in range(twoPos, len(arr)):
  if parse_lists([[6]], arr[i].copy()):
    sixPos = i+2
    break

print(twoPos * sixPos)