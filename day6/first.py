#This is not completely my own solution

g = {i+j*1j: c for i, r in enumerate(open('input6.txt'))
               for j, c in enumerate(r.strip())}

start = min(p for p in g if g[p] == '^')

def walk(g):
    pos, dir, seen = start, -1, set()
    while pos in g and (pos, dir) not in seen:
        seen |= {(pos, dir)}
        if g.get(pos+dir) == '#':
            dir *= -1j
        else: pos += dir
    return {p for p,_ in seen}, (pos, dir) in seen

path = walk(g)[0]
print(len(path), sum(walk(g | {o : '#'}) [1] for o in path))