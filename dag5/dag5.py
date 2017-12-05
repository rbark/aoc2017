instructions = []
jumps = 0
with open('input.txt') as file:
    for line in file.readlines():
        instructions.append(int(line))

current_pos = 0

try:
    while True:
        tmp = instructions[current_pos]
        instructions[current_pos] = tmp+1
        current_pos += tmp
        jumps+=1
except:
    print(jumps)