with open('input.txt') as file:
    puzzle = file.readlines()



def part1():

    checksum = 0
    for line in puzzle:
        numberList = list(map(int, (line.split())))
        checksum += int(max(numberList)) - int(min(numberList))

    print(checksum)


def part2():
    checksum = 0
    for line in puzzle:
        numberList = list(map(int, (line.split())))
        numberList.sort(reverse=True)
        for i in range(len(numberList)):
            for j in range(i+1, len(numberList)):
                if numberList[i] % numberList[j] == 0:
                    checksum += numberList[i] / numberList[j]
                    break
    print(checksum)


part2()