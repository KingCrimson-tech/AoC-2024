from collections import defaultdict

p1, p2 = open('input5.txt').read().split('\n\n')
updates = [list(map(int, line.split(','))) for line in p2.splitlines()]
# print(updates)

orders = defaultdict(list)
for order in p1.splitlines():
    before, after = order.split('|')
    orders[int(before)].append(int(after))

res1 = 0
res2 = 0
for pages in updates:
    sorted_pages = sorted(pages, key=lambda page: -len([order for order in orders[page] if order in pages]))
    if pages == sorted_pages:
        res1 += pages[len(pages) // 2] 
    else:
        res2 += sorted_pages[len(sorted_pages) // 2]

print(res1)
print(res2)