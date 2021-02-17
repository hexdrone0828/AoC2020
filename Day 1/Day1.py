_input = open("input.txt", "r").readlines()
_input = [int(i) for i in _input]
_input.sort()
for x in _input:
    for y in reversed(_input):
        if x + y == 2020:
            print(x + y)
            print(x*y)

for x in _input:
    for y in _input:
        for z in _input:
            if x + y + z == 2020:
                print(x + y + z)
                print(x*y*z)