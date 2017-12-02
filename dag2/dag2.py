with open('input.txt') as file:
    puzzle = file.readlines()


checksum = 0

for line in puzzle:
    numberList = list(map(int, (line.split())))
    checksum += int(max(numberList)) - int(min(numberList))

print(checksum)