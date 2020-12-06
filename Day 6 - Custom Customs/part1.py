inputFile = open("input.txt", "r")
lines = inputFile.readlines()

countSum = 0
currentCount = 0
yesQuestions = {}

for line in lines:
  line = line.rstrip("\r\n")

  for char in line:
    if char not in yesQuestions:
      currentCount += 1
      yesQuestions[char] = True

  if line == "":
    countSum += currentCount
    currentCount = 0
    yesQuestions = {}



print(countSum)