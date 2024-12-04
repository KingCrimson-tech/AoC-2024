words = []
with open('input4.txt', 'r') as f:
    for line in f.readlines():
        words.append(list(line.strip()))
n = len(words)

def in_bound(i, j):
    return 0 <= i < n and 0 <= j < n

res = 0
for i in range(n):
    for j in range(n):
        if words[i][j] != 'X':
            continue
        for p in [-1, 0, 1]:
            for q in [-1, 0, 1]:
                if (p, q) == (0, 0):
                    continue
                if in_bound(i+3*p, j+3*q):
                    if ''.join(words[i+k*p][j+k*q] for k in range(4)) == 'XMAS':
                        res += 1

print(res)