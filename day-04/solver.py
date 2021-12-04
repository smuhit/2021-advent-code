data = [x for x in open('input.txt').read().split('\n')]

numbers = [int(x) for x in data[0].split(',')]

boards = []

for line_number in range(2, len(data), 6):
    board = [int(x) for line in data[line_number:line_number+5] for x in line.split() ]
    boards.append(board)

def is_winner(board):
    for x in range(5):
        if all(y == 'X' for y in board[5 * x:5 * x + 5]):
            return True
        if all(y == 'X' for y in [board[x], board[x + 5], board[x + 10], board[x + 15], board[x + 20]]):
            return True
    return False

found = []
boards_won = set()
for number in numbers:
    for i, board in enumerate(boards):
        if i in boards_won:
            continue
        for j, x in enumerate(board):
            if x == number:
                board[j] = 'X'
                if is_winner(board):
                    found.append((i, number))
                    boards_won.add(i)
                break
    if len(boards_won) >= len(boards):
        break

# Part 1
print(sum(filter(lambda x: x != 'X', boards[found[0][0]])) * found[0][1])

# Part 2
print(sum(filter(lambda x: x != 'X', boards[found[-1][0]])) * found[-1][1])
