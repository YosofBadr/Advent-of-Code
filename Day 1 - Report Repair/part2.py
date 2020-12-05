inputFile = open("input.txt", "r")

inputArray = []
targetSum = 2020

for line in inputFile:
  inputArray.append(int(line))


inputArray.sort()

for i in range(len(inputArray) - 2):
  leftIdx = i + 1
  rightIdx = len(inputArray) - 1
  
  while leftIdx < rightIdx:
    currSum = inputArray[i] + inputArray[leftIdx] + inputArray[rightIdx]

    if currSum == targetSum:
      print(inputArray[i] * inputArray[leftIdx] * inputArray[rightIdx])
      break
    elif currSum < targetSum:
      leftIdx += 1
    else:
      rightIdx -= 1
