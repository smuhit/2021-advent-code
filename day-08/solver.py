data = [x.rstrip() for x in open('input.txt').read().splitlines()]


# Part 1
count = 0
output_map = {
    2: lambda: 1,
    3: lambda: 1,
    4: lambda: 1,
    7: lambda: 1,
}
for line in data:
    output = line.split('|')[-1]
    for part in output.split():
        count += output_map.get(len(part), lambda: 0)()

print(count)

# Part 2
def determine_digits(input_digits, output_digits):
    digits_segments = [[] for _ in range(7)]
    for digit in input_digits:
        digits_segments[len(digit) - 1].append(set(digit))

    digit_map = {x[1]: digits_segments[x[0]][0] for x in [(1, 1), (2, 7), (3, 4), (6, 8)]}
    for digit in digits_segments[5]:
        if digit_map[7] - digit:
            digit_map[6] = digit
        elif digit_map[4] - digit:
            digit_map[0] = digit
        else:
            digit_map[9] = digit
    for digit in digits_segments[4]:
        if not(digit_map[7] - digit):
            digit_map[3] = digit
        elif not(digit - digit_map[9]):
            digit_map[5] = digit
        else:
            digit_map[2] = digit

    reverse_map = {frozenset(digit_map[x]): str(x) for x in digit_map}

    digits = ""
    for digit in output_digits:
        digits += reverse_map[frozenset(digit)]

    return int(digits)

total = 0
for line in data:
    input_part, output_part = line.split('|')
    input_digits = input_part.split()
    output_digits = output_part.split()
    total += determine_digits(input_digits, output_digits)
print(total)
