data = [x for x in open('input.txt').read().split()]

# Part 1
length = len(data[0])
gamma = ""
epsilon = ""
for i in range(length):
    num_zero = sum(1 for datum in data if datum[i] == '0')
    num_one = sum(1 for datum in data if datum[i] == '1')
    if num_one > num_zero:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, base=2) * int(epsilon, base=2))

# Part 2

def find_it(filter_fn):
    current = 0
    considerations = data
    while len(considerations) > 1:
        num_zero = sum(1 for datum in considerations if datum[current] == '0')
        num_one = sum(1 for datum in considerations if datum[current] == '1')
        considerations = list(filter(lambda x: x[current] == filter_fn(num_zero, num_one), considerations))
        current += 1
    return considerations[0]

oxygen = find_it(lambda x, y: '1' if y >= x else '0')
co2 = find_it(lambda x, y: '0' if y >= x else '1')
print(int(oxygen, base=2) * int(co2, base=2))
