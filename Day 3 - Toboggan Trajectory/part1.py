def slopes(right, down):
  inputFile = open("input.txt", "r")
  currChar = 0
  treesEncountered = 0  
  inc = right
  for lineNum, line in enumerate(inputFile):
    if lineNum % down == 0:
      line = line.rstrip("\n")
      line = line.rstrip()

      numChars = len(line) 

      if line[currChar % numChars] == "#":
        treesEncountered += 1
      currChar += inc

  return treesEncountered

print(slopes(1, 1) * slopes(3, 1) * slopes(5, 1) * slopes(7, 1) * slopes(1, 2))
