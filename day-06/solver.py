data = [int(x) for x in open('input.txt').read().split(',')]

fish_days = [0 for x in range(9)]
for x in data:
    fish_days[x] += 1

def span_days(fish_days, num):
    for _ in range(num):
        fish_zero = fish_days[0]
        for idx, fish in enumerate(fish_days[1:]):
            fish_days[idx] = fish
        fish_days[-1] = fish_zero
        fish_days[6] += fish_zero

# Part 1
fish_days_part_1 = fish_days.copy()
span_days(fish_days_part_1, 80)
print(sum(fish_days_part_1))

# Part 2
fish_days_part_2 = fish_days.copy()
span_days(fish_days_part_2, 256)
print(sum(fish_days_part_2))
