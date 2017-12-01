

with open('input.txt') as file:
    puzzle = file.read()


hash= str(puzzle)
puzzle_length = len(str(hash))

# del 1
# result = sum(int(hash[i]) for i in range(puzzle_length) if hash[i] == hash[(i + 1) % puzzle_length])

result = sum(int(hash[i]) for i in range(puzzle_length) if hash[i] == hash[(i + puzzle_length//2)  % puzzle_length])


print(result)