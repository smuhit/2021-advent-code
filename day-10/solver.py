data = [x for x in open('input.txt').read().split()]

matching = {'(': ')', '[': ']', '{': '}', '<': '>'}

# Part 1
point_value = {')': 3, ']': 57, '}': 1197, '>': 25137}
incorrect_lines = set()  # for Part 2 so I don't need to parse them again
value = 0
for idx, line in enumerate(data):
    stack = []
    for char in line:
        if char in matching:
            stack.append(char)
        else:
            previous = stack.pop()
            if char != matching[previous]:
                incorrect_lines.add(idx)
                value += point_value[char]
                break
print(value)

# Part 2
point_value = {'(': 1, '[': 2, '{': 3, '<': 4}
all_values = []
for idx, line in enumerate(data):
    if idx in incorrect_lines:
        continue
    value = 0
    stack = []
    for char in line:
        if char in matching:
            stack.append(char)
        else:
            stack.pop()
    for char in stack[::-1]:
        value = value * 5 + point_value[char]
    all_values.append(value)
all_values.sort()
print(all_values[len(all_values) // 2])
