instructions = []
jumps = 0
with open('input.txt') as file:
    for line in file.readlines():
        instructions.append(int(line))

current_pos = 0

def part1():
    global instructions, current_pos, jumps
    try:
        while True:
            tmp = instructions[current_pos]
            instructions[current_pos] = tmp + 1
            current_pos += tmp
            jumps += 1
    except:
        print(jumps)


def part2():
    global instructions, current_pos, jumps
    jumps = 0
    try:
        while True:
            tmp = instructions[current_pos]
            if tmp > 2:
                replace = tmp -1
            else:
                replace = tmp + 1
            instructions[current_pos] = replace
            current_pos += tmp
            jumps += 1
    except:
        print(jumps)


#part1()
part2()