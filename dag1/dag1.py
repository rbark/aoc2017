

with open('input.txt') as file:
    puzzle = file.read()


print(puzzle)
hash= str(puzzle)
puzzle_length = len(str(hash))

result = sum(int(hash[i]) for i in range(puzzle_length) if hash[i] == hash[(i + 1) % puzzle_length])


print(result)