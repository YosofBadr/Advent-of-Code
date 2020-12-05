def checkRange(num, minimum, maximum):
  num = int(num)

  if minimum <= num <= maximum:
    return True
  
  return False

inputFile = open("input.txt", "r")
lines = inputFile.readlines()

numberValid = 0
requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "pid", "ecl"]
fields = {}
validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
validHcl = "0123456789abcdef"
isValid = True
for line in lines:
  line = line.rstrip("\r\n")
  attributes = line.split(" ")

  if line != "":
    for attribute in attributes:
      newField = attribute.split(":")
      fields[newField[0]] = newField[1]
  else:
    for requirement in requirements:
      if requirement not in fields:
        isValid = False
        break

      if requirement == "byr":
        if (not checkRange(fields[requirement], 1920, 2002)):
          isValid = False
          break
      elif requirement == "iyr":
        if (not checkRange(fields[requirement], 2010, 2020)):
          isValid = False
          break
      elif requirement == "eyr":
        if (not checkRange(fields[requirement], 2020, 2030)):
          isValid = False
          break
      elif requirement == "hgt":
        if "cm" in fields[requirement]:
          minimum = 150
          maximum = 193
        else:
          minimum = 59
          maximum = 76

        height = fields[requirement][:-2]
        if (not checkRange(height, minimum, maximum)):
          isValid = False
          break
      elif requirement == "hcl":
        if (fields[requirement][0] == "#" and len(fields[requirement]) == 7):
          for i in range(1, 7):
            if fields[requirement][i] not in validHcl:
              isValid = False
              break   
        else:
          isValid = False
          break   
      elif requirement == "ecl":
        if (fields[requirement] not in validEcl):
          isValid = False
          break    
      elif requirement == "pid":
        if (len(fields[requirement]) != 9):
          isValid = False
          break         

    if isValid:
      numberValid += 1

    isValid = True
    fields = {}
    
print(numberValid) 
