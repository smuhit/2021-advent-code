data = [int(x) for x in open('input').read().split()]

# Part 1
print(sum(1 if data[i] > data[i - 1] else 0 for i in range(1, len(data))))

# Part 2
print(sum(1 if data[i] + data[i - 1] + data [i - 2] > data[i - 1] + data[i - 2] + data [i - 3] else 0 for i in range(3, len(data))))