right = list()
left = list()

with open('input.txt', 'r') as f:
    for line in f:
        l, r = line.split()
        right.append(int(r))
        left.append(int(l))

left.sort()
right.sort()

sim_score = 0

for i in left:
    j = right.count(i)
    sim_score += i * j

print(sim_score)