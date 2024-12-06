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
    exit()

def loop(grid, r, c):
    dr = -1
    dc = 0
    seen = set()

    while True:
        seen.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols: return False
        if grid[r + dr][c + dc] == '#':
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in seen:
            return True
        
count = 0

for cr in range(rows):
    for cc in range(cols):
        if grid[cr][cc] != '.': continue
        grid[cr][cc] = '#'
        if loop(grid, r, c):
            count += 1
        grid[cr][cc] = '.'

print(count)