BLANK = "#"

def read_sudoku(filename):
    """
    스도쿠 퍼즐이 저장된 파일을 읽어 2차원 리스트 형태로 반환한다.

    Parameters:
        filename (str): 스도쿠 퍼즐이 저장된 텍스트 파일 경로

    Returns:
        list[list[str]]: 9행 9열의 스도쿠 보드. 각 요소는 '1'~'9' 또는 빈 칸을 의미하는 '#'.

    예시:
        파일 내용:
        53#  ##7  ###
        6##  195  ###
        #98  ###  #6#

        -> 반환값:
        [['5', '3', '#', ..., '#'],
         ['6', '#', '#', ..., '#'],
         ['#', '9', '8', ..., '#'],
         ...
        ]
    """
    pass

def is_current_board_valid(board):
    """
    현재 보드(board)가 스도쿠의 규칙에 맞는지 검사한다.
    - 행, 열, 3x3 박스 내에 중복된 숫자가 없어야 함

    Parameters:
        board (list[list[str]]): 스도쿠 보드

    Returns:
        bool: 유효하면 True, 중복이 있으면 False

    예시:
        is_current_board_valid([
            ['5','3','#','#','7','#','#','#','#'],
            ['6','#','#','1','9','5','#','#','#'],
            ...
        ]) -> True
    """
    pass

def is_valid_set_of_chunk(chunk):
    """
    하나의 행, 열 또는 3x3 박스를 나타내는 9개의 셀 리스트가 유효한지 확인한다.
    - '#'은 무시하고 숫자만 비교
    - 중복이 없으면 True 반환

    Parameters:
        chunk (list[str]): 9개의 셀 (ex: 한 행, 한 열, 또는 한 박스)

    Returns:
        bool: 유효하면 True, 중복이 있으면 False

    예시:
        is_valid_set_of_chunk(['1','2','#','3','4','#','5','6','7']) -> True
        is_valid_set_of_chunk(['1','2','2','#','#','#','#','#','#']) -> False
    """
    pass

def get_boxes(board):
    """
    9x9 보드에서 3x3 박스 9개를 추출하여 리스트로 반환한다.
    - 각 박스는 왼쪽 위부터 오른쪽 아래 순서로 진행

    Parameters:
        board (list[list[str]]): 스도쿠 보드

    Returns:
        list[list[str]]: 3x3 박스 9개. 각 박스는 9개의 문자열을 가진 리스트.

    예시:
        get_boxes(board)[0] -> board[0][0:3] + board[1][0:3] + board[2][0:3]
    """
    pass

def get_empty_cells(board):
    """
    현재 보드에서 빈 칸('#')의 위치를 모두 찾아 좌표로 반환한다.

    Parameters:
        board (list[list[str]]): 스도쿠 보드

    Returns:
        list[tuple[int, int]]: 빈 칸의 좌표 목록. 각 항목은 (행 인덱스, 열 인덱스)

    예시:
        get_empty_cells([
            ['5','3','#','#','7','#','#','#','#'],
            ['6','#','#','1','9','5','#','#','#'],
            ...
        ]) -> [(0,2), (0,3), (0,5), (0,6), ...]
    """
    pass

def solve_sudoku(board):
    """
    주어진 스도쿠 보드를 완성한다. (백트래킹 방식 사용)

    Parameters:
        board (list[list[str]]): 9x9 스도쿠 보드. BLANK(`#`)는 빈 칸.

    Returns:
        bool: 해를 찾았으면 True, 불가능하면 False

    동작:
        - 가능한 숫자(1~9)를 하나씩 시도하며 유효성 검사를 한다.
        - 재귀적으로 다음 빈 칸을 채운다.
        - 해가 존재할 경우 board를 직접 수정하여 완성된 결과를 남긴다.
        - board 자체가 수정됨에 유의할 것! (원본이 변경됨)

    예시:
        board = [
            ['5','3','#','#','7','#','#','#','#'],
            ['6','#','#','1','9','5','#','#','#'],
            ...
        ]
        solve_sudoku(board)
        -> True (그리고 board는 해답으로 덮어씌워짐)
    """
    pass

def print_board(board):
    for row in board:
        print(' '.join(row))

# 실행 예시:
board = read_sudoku('sudoku.txt')
if solve_sudoku(board):
    print_board(board)
