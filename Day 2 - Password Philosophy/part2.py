inputFile = open("input.txt", "r")

numOfValidPassword = 0

for line in inputFile:
  occurences = 0
  line = line.split(" ")

  policy = line[0].split("-")
  idxOne = int(policy[0]) - 1
  idxTwo = int(policy[1]) - 1

  targetChar = line[1].replace(':', '')
  password = line[2]

  charOne = password[idxOne] == targetChar
  charTwo = password[idxTwo] == targetChar
  
  if  charOne ^ charTwo:
    numOfValidPassword += 1


print(numOfValidPassword)