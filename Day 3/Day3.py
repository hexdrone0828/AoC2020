#part 1
with open ("input.txt", "r") as _input:
    lines = [line.rstrip() for line in _input] 

charlength = len(lines[0])
position = 0
speed = 3

treecount = 0
for line in lines:
    if line[position%charlength] == "#":
        treecount += 1
    position = position + speed

print("The collision count for Part 1 is " +str(treecount))

#part 2

speed = [[1,1], [3,1], [5,1], [7,1], [1,2]]
multipliedcount = 1
for velocity in speed:
    position = 0
    treeCount = 0
    lines = lines[0::velocity[1]]
    for line in lines:
        if line[position%charlength] == "#":
            treecount +=1
        position = position + velocity[0]
    cultipliedcount = multipliedcount * treecount

print("The multiplied count for part 2 is " +str(multipliedcount))