from collections import defaultdict

# nästan kopierat rakt av från http://www.cdn.geeksforgeeks.org/find-coordinates-prime-number-prime-spiral/

def spiralSplicer(inp):
    # Batch size tracker
    step_count = 1

    # Batch size limiter
    step_limit = 2

    # switches between -1 and +1
    adder = 1

    # Co-ordinates of step K
    x, y = 0, 0

    for n in range(2, inp + 1):

        # Keeps track of steps
        # Checks on the current batch
        if (step_count <= .5 * step_limit):
            x += adder  # Switch to operating on x

        elif (step_count <= step_limit):
            y += adder  # Switch to operating on x

        if (step_count == step_limit):
            # Changes adder to -1 and vice versa
            adder *= -1

            # Keeps on updating 'step_limit'
            step_limit += 2

            # Resets count
            step_count = 0
        step_count += 1
    print(abs(x) + abs(y))

def get_next(spiral , coord):
    x, y = coord

    next_move = ()
    # höger  vänster inte tom och upp inte tom
    if spiral[(x+1, y)] == 0 and spiral[(x, y + 1)] != 0:
        next_move =  (x+1, y)
    # upp  vänster inte tom, upp tom
    elif spiral[(x-1, y)] != 0 and spiral[(x, y+1)] == 0:
        next_move = (x, y+1)
    #  ner upp inte tom, höger inte tom
    elif spiral[(x+1, y)] != 0 and spiral[(x, y-1)] == 0:
        next_move = (x, y - 1)
    # vänster
    else:
        next_move = (x-1, y)
    return next_move

def part1(number):

    currentNumber = 1
    coord=(0, 0)
    spiral = defaultdict(int)
    spiral[coord] = currentNumber
    currentNumber +=1
    coord=(1, 0)
    spiral[coord] = currentNumber
    while currentNumber != number:
        currentNumber +=1
        coord = get_next(spiral, coord )
        spiral[coord] = currentNumber
    x, y = coord

    print(abs(x) + abs(y))



# spiralSplicer(277678)
part1(277678)