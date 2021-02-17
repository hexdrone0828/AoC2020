import re

_input = open("input.txt", "r").read().split('\n')
validcounter = 0

#part 1
for x in _input:
    instructions = re.split("[-: ]+", x)
    if int(instructions[0]) <= instructions[3].count(instructions[2]) <= int(instructions[1]):
        validcounter += 1
print(f"The answer for part 1 is: {validcounter}")

#part 2
validcounter = 0
for x in _input:
    instructions = re.split("[-: ]+", x)
    password = list(instructions[3])
    if bool(password[int(instructions[0])-1] == instructions[2]) ^ bool(password[int(instructions[1])-1] == instructions[2]):
        validcounter += 1
print(f"The answer for part 2 is: {validcounter}")
    