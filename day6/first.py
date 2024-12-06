with open('input6.txt') as f:
    grid = list(map(list, f.read().splitlines()))

rows = len(grid)
cols = len(grid[0])

found = False
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '^':
            found = True
            break
    if found:
        break
else:
    print('No')

dr = -1
dc = 0

seen = set()

while True:
    seen.add((r, c))
    if not (0 <= r + dr <= rows and 0 <= c + dc <= cols): break
    if grid[r + dr][c + dc] == '#':
        dc, dr = -dr, dc
    else:
        r += dr
        c += dc

print(len(seen))