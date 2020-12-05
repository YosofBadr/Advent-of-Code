import math

inputFile = open("input.txt", "r")
lines = inputFile.readlines()

highestSeatID = float('-inf')

for line in lines:
  line = line.rstrip("\r\n")

  rowMin = 0 
  rowMax = 127

  for charIdx in range(0, 7):
    char = line[charIdx]

    midPoint = (rowMax + rowMin)/2.0
    if char == "F":
      rowMax = math.floor(midPoint)
      row = rowMax
    else:
      rowMin = math.ceil(midPoint)
      row = rowMin
#====================================================
  colMin = 0 
  colMax = 7

  for charIdx in range(7, 10):
    char = line[charIdx]

    midPoint = (colMin + colMax)/2.0

    if char == "L":
      colMax = math.floor(midPoint)
      col = colMax
    else:
      colMin = math.ceil(midPoint)
      col = colMin

  currentSeatID = row * 8 + col

  if currentSeatID > highestSeatID:
    highestSeatID = currentSeatID

print(highestSeatID)