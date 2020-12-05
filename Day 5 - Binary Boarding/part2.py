import math

inputFile = open("input.txt", "r")
lines = inputFile.readlines()

seatList = []

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
  seatList.append(currentSeatID)

seatList.sort()
for i in range(0, len(seatList)):
  if seatList[i] + 1 != seatList[i + 1]:
    print(seatList[i] + 1)
    break 