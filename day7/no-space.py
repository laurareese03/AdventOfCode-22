import json

MAX_DISK_SPACE = 70000000
DISK_SPACE_NEEDED = 30000000

with open('commands.txt') as f:
  lines = f.readlines()

def iterate_dict(d, term):
  for key, value in d.items():
    if(value == term):
      return d
  for key, value in d.items():
    holder = None
    if type(value) is dict:
      holder = iterate_dict(value, term)
    if holder != None:
      return holder

def get_folder_size(d, folderSize):
  for key, value in d.items():
    if type(value) is not  dict:
      folderSize += int(value)
    else: 
      folderSize = get_folder_size(d[key], folderSize)
  return folderSize

def get_all_folders_sizes(d, sizeArray):
  sizeArray.append(get_folder_size(d, 0))
  for key, value in d.items():
    if type(value) is dict:
      get_all_folders_sizes(d[key], sizeArray)
  return sizeArray

def get_total_folder_sizes(sizes):
  totalSize = 0
  for size in sizes:
    if size < 100000:
      totalSize += size
  return totalSize

def part_b(folderSizes):
  folderSizes.sort()
  spaceAvailable = MAX_DISK_SPACE - folderSizes[-1]
  for folder in folderSizes:
    if spaceAvailable + folder > DISK_SPACE_NEEDED:
      print(folder)
      break

def part_a():
  currentDict = {}
  overallDict = currentDict
  for line in lines:
    line = line.strip()
    # handle directory change command
    if line[0:4] == '$ cd':
      # get next deeper directory
      if line[5:] != '..':
        currentDict.update({line[5:]: {}})
        currentDict = currentDict[line[5:]]
      # get layer shallower directory
      else:
        currentDict = iterate_dict(overallDict, currentDict)
    # handle list command
    elif line[0:1] != '$':
      if line[0:3] != 'dir':
        file = line.split(' ')
        currentDict.update({file[1]: file[0]})

  res = json.dumps(overallDict, sort_keys=True, indent=4)

  finalArray = get_all_folders_sizes(overallDict['/'], [])
  print(get_total_folder_sizes(finalArray))
  part_b(finalArray)


part_a()