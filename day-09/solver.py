data = [x for x in open('input.txt').read().split()]

# Part 1
low_points = []
max_y = len(data)
max_x = len(data[0])
for i in range(max_y):
    for j in range(max_x):
        current = int(data[i][j])
        if i > 0 and current >= int(data[i - 1][j]):
            continue
        if j > 0 and current >= int(data[i][j - 1]):
            continue
        if i < max_y - 1 and current >= int(data[i + 1][j]):
            continue
        if j < max_x - 1 and current >= int(data[i][j + 1]):
            continue
        low_points.append((i, j, current))

print(sum(x[2] for x in low_points) + len(low_points))

# Part 2
from functools import reduce

def find_basin_size(x, y, visited=set()):
    if x < 0 or x >= max_x:
        return 0
    if y < 0 or y >= max_y:
        return 0
    if int(data[y][x]) == 9:
        return 0
    count = 1
    visited.add((x, y))
    for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if (a, b) not in visited:
            count += find_basin_size(a, b, visited)
    return count

basin_sizes = []
for y, x, _ in low_points:
    basin_sizes.append(find_basin_size(x, y))
basin_sizes.sort(reverse=True)
print(reduce(lambda a, b: a * b, basin_sizes[:3]))
