import re

with open('input3.txt', 'r') as f:
    data = f.read().strip()

match = re.findall(r"mul\((\d+),(\d+)\)", data)

res = sum(int(i) * int(j) for i, j in match)
print(res)