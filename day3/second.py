import re

with open('input3.txt', 'r') as f:
    data = f.read().strip()

res = 0
do = data.split("do()")
print(do)
for i in do:
    d = i.split("don't()")[0]
    res += sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", d))

print(res)