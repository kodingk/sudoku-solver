BLANK = "#"

def read_sudoku(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def is_current_board_valid(board):
    for row in board:
        if not is_valid_set_of_chunk(row):
            return False

    for col in zip(*board):
        if not is_valid_set_of_chunk(col):
            return False

    for box in get_boxes(board):
        if not is_valid_set_of_chunk(box):
            return False

    return True

def is_valid_set_of_chunk(chunk):
    chunk = [cell for cell in chunk if cell != BLANK]
    return len(chunk) == len(set(chunk))

def get_boxes(board):
    boxes = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            boxes.append(box)
    return boxes

def get_empty_cells(board):
    empty_cells = []
    for rdx, row in enumerate(board):
        for cdx, cell in enumerate(row):
            if cell == BLANK:
                empty_cells.append((rdx, cdx))
    return empty_cells

def solve_sudoku(board):
    if not is_current_board_valid(board):
        return False

    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return True

    rdx, cdx = empty_cells[0]
    for num in range(1, 10):
        board[rdx][cdx] = str(num)
        if solve_sudoku(board):
            return True
        board[rdx][cdx] = BLANK

    return False

def print_board(board):
    for row in board:
        print(' '.join(row))

board = read_sudoku('sudoku.txt')
if solve_sudoku(board):
    print_board(board)
