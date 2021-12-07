data = [int(x) for x in open('input.txt').read().split(',')]

max_crab = max(data)
min_crab = min(data)

# Part 1 
min_fuel = None
for x in range(min_crab, max_crab):
    cur_fuel = 0
    for y in data:
        cur_fuel += abs(y - x)
    if min_fuel is None or cur_fuel < min_fuel:
        min_fuel = cur_fuel

print(min_fuel)

# Part 1 
min_fuel = None
for x in range(min_crab, max_crab):
    cur_fuel = 0
    for y in data:
        cur_rate = abs(y - x)
        cur_fuel += cur_rate * (cur_rate + 1) // 2
    if min_fuel is None or cur_fuel < min_fuel:
        min_fuel = cur_fuel

print(min_fuel)
