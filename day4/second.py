words = []

with open('input4.txt') as f:
    for line in f.readlines():
        words.append(list(line.strip()))
n = len(words)

def in_bound(i, j):
    return 0 <= i < n and 0 <= j < n

res = 0
for i in range(n):
    for j in range(n):
        if words[i][j] != 'A':
            continue
        if not in_bound(i+1, j+1):
            continue
        if not in_bound(i+1, j-1):
            continue
        if not in_bound(i-1, j+1):
            continue
        if not in_bound(i-1, j-1):
            continue
        if not (words[i-1][j-1], words[i+1][j+1]) in (('M', 'S'), ('S', 'M')):
            continue
        if not (words[i+1][j-1], words[i-1][j+1]) in (('M', 'S'), ('S', 'M')):
            continue
        res += 1

print(res) 