reports = list()

with open('input.txt', 'r') as f:
    l = f.readlines()
l = [el.replace('\n', '') for el in l]

levels = list()

for i in range(len(l)):
    temp = [int(n) for n in l[i].split(' ')]
    levels.append(temp)

count = 0
for level in levels:
    safe1 = all(i < j and 1 <= (j - i) <= 3 for i, j in zip(level, level[1:]))
    safe2 = all(i > j and 1<= (i - j) <= 3 for i, j in zip(level, level[1:]))

    if safe1 or safe2:
        count += 1

print(count)
    

