inputFile = open("input.txt", "r")

numOfValidPassword = 0

for line in inputFile:
  occurences = 0
  line = line.split(" ")

  policy = line[0].split("-")
  minOcc = int(policy[0])
  maxOcc = int(policy[1])

  targetChar = line[1].replace(':', '')
  password = line[2]


  for char in password:
    if char == targetChar:
      occurences += 1

  if  minOcc<= occurences <= maxOcc:
    numOfValidPassword += 1


print(numOfValidPassword)