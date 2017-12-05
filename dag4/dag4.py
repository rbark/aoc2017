words = []

valid_lines = 0

with open("input.txt") as f:
    for line in f.readlines():
        wordlist = line.strip().split(' ')
        wordset = set(wordlist)
        if len(wordset) == len(wordlist):
            valid_lines += 1

valid_passphrase = 0

with open("input.txt") as f:
    for line in f.readlines():
        wordlist = line.strip().split(' ')
        sortedChars = [''.join(sorted(w)) for w in wordlist]
        wordset = set(sortedChars)
        if len(wordset) == len(wordlist):
            valid_passphrase += 1


print(valid_lines)
print(valid_passphrase)
