data = [x for x in open('input.txt').read().split('\n')]

# Part 1

horiz = depth = 0

verb_map = {
    'forward' : lambda x: (horiz + x, depth),
    'down': lambda x: (horiz, depth + x),
    'up': lambda x: (horiz, depth - x),
}

for datum in data:
    verb, amount = datum.split(' ')
    horiz, depth = verb_map[verb](int(amount))

print(horiz * depth)

# Part 2

aim = horiz = depth = 0

verb_map = {
    'forward' : lambda x: (horiz + x, depth + (aim * x), aim),
    'down': lambda x: (horiz, depth, aim + x),
    'up': lambda x: (horiz, depth, aim - x),
}

for datum in data:
    verb, amount = datum.split(' ')
    horiz, depth, aim = verb_map[verb](int(amount))

print(horiz * depth)
