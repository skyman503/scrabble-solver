from itertools import combinations, permutations

FILENAME = ""

file = open(FILENAME, encoding="utf-8")

data = set()
for i in file.readlines():
    data.add(i.rstrip())

letters = [i for i in input().lower()]

matches = []

for i in range(1, len(letters)+1):
    for j in combinations(letters, i):
        for k in permutations(j):
            word = ''.join(k)
            if word in data:
                matches.append(word)

print(matches)
