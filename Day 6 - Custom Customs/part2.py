inputFile = open("input.txt", "r")
lines = inputFile.readlines()

countSum = 0
questionFrequency = {}
groupSize = 0

for line in lines:
  line = line.rstrip("\r\n")

  if line != "":
    groupSize += 1
    for char in line:
      if char in questionFrequency:
        questionFrequency[char] += 1
      else:
        questionFrequency[char] = 1
  else:
    for key, value in questionFrequency.items():
      if value == groupSize:
        countSum += 1
    questionFrequency = {}
    groupSize = 0

print(countSum)