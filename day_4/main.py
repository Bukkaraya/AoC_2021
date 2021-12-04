def mark_value(board, mask, value):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == value:
                mask[i][j] = 'x'


def is_bingo(mask):
    for line in mask:
        if line.count("x") == len(line):
            return True

    mask_transposed = list(map(list, zip(*mask)))

    for line in mask_transposed:
        if line.count("x") == len(line):
            return True

    return False


def get_sum_of_unmarked_numbers(board, mask):
    total = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if mask[i][j] != 'x':
                total += board[i][j]

    return total

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        bingo_input = f.read().split("\n")

    values = [int(i) for i in bingo_input[0].split(",")]
    bingo_boards = bingo_input[2:]
    boards = []

    for i in range((len(bingo_boards) // 6) + 1):
        current_board = bingo_boards[i * 6:i * 6 + 5]
        for i in range(len(current_board)):
            current_board[i] = [int(l) for l in current_board[i].split()]
        boards.append(current_board)

    minimum_iterations_for_bingo = 1000000
    maximum_iterations_for_bingo = 0

    for board in boards:
        mask = [['' for _ in range(5)] for _ in range(5)]
        iterations_for_bingo = 0
        for value in values:
            mark_value(board, mask, value)
            iterations_for_bingo += 1

            if is_bingo(mask):
                if iterations_for_bingo < minimum_iterations_for_bingo:
                    first_winner_info = (value, board, mask)
                    minimum_iterations_for_bingo = iterations_for_bingo

                if iterations_for_bingo > maximum_iterations_for_bingo:
                    last_winner_info = (value, board, mask)
                    maximum_iterations_for_bingo = iterations_for_bingo
                break


    value, board, mask = first_winner_info
    unmarked_numbers_sum = get_sum_of_unmarked_numbers(board,
                                                       mask)
    print(f"Result for Part 1: {unmarked_numbers_sum * value}")

    value, board, mask = last_winner_info
    unmarked_numbers_sum = get_sum_of_unmarked_numbers(board,
                                                       mask)
    print(f"Result for Part 1: {unmarked_numbers_sum * value}")


