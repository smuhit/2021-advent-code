from collections import defaultdict

data = [x for x in open('input.txt').read().split() if x != '->']

points = [tuple(int(x) for x in point.split(',')) for point in data]

visited = defaultdict(lambda: 0)

# Part 1

for i in range(0, len(points), 2):
    x = points[i]
    y = points[i + 1]
    if x[0] == y[0]:
        current = x[1]
        visited[(x[0], current)] += 1
        incrementor = 1 if x[1] < y[1] else -1
        while current != y[1]:
            current += incrementor
            visited[(x[0], current)] += 1
    elif x[1] == y[1]:
        current = x[0]
        visited[(current, x[1])] += 1
        incrementor = 1 if x[0] < y[0] else -1
        while current != y[0]:
            current += incrementor
            visited[(current, x[1])] += 1
print(sum(1 for x in visited if visited[x] >= 2))

# Part 2

for i in range(0, len(points), 2):
    x = points[i]
    y = points[i + 1]
    if x[0] == y[0] or x[1] == y[1]:
        continue
    cur_x = x[0]
    x_inc = 1 if x[0] < y[0] else -1
    cur_y = x[1]
    y_inc = 1 if x[1] < y[1] else -1
    visited[(cur_x, cur_y)] += 1
    while cur_x != y[0] or cur_y != y[1]:
        cur_x += x_inc
        cur_y += y_inc
        visited[(cur_x, cur_y)] += 1
print(sum(1 for x in visited if visited[x] >= 2))
