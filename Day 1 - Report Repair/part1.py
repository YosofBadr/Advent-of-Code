inputFile = open("input.txt", "r")

numHash = {}
targetSum = 2020

for line in inputFile:
  currNum = int(line)
  possibleMatch = targetSum - currNum

  if possibleMatch in numHash:
    print(possibleMatch * currNum)
  else:
    numHash[currNum] = True