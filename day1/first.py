right = list()
left = list()

with open('input.txt', 'r') as f:
    for line in f:
        l, r = line.split()
        right.append(int(r))
        left.append(int(l))

left.sort()
right.sort()

distance = 0

for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)