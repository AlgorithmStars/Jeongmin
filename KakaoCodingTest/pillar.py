

PILLAR, CROSSBEAM = 0, 1


def solution(n:int, build_frame:list[list]):
    global PILLAR, CROSSBEAM

    def checkValid(board, x, y, bType):
        if bType == PILLAR:
            if y == 0 or\
                    board[x-1][y][CROSSBEAM] or board[x][y][CROSSBEAM] or\
                    board[x][y-1][PILLAR]:
                return True
        if bType == CROSSBEAM:
            if board[x][y-1][PILLAR] or board[x+1][y-1][PILLAR] or\
                    (board[x-1][y][CROSSBEAM] and board[x+1][y][CROSSBEAM]):
                return True
        return False

    def insert(board, x, y, bType):
        if checkValid(board, x, y, bType):
            board[x][y][bType] = True


    def delete(board, x, y, bType):
        board[x][y][bType] = False

        for i, line in enumerate(board):
            for j, element in enumerate(line):
                if (element[PILLAR] and not checkValid(board, i, j, PILLAR)) or\
                        (element[CROSSBEAM] and not checkValid(board, i, j, CROSSBEAM)):

                    board[x][y][bType] = True
                    return

    answer = []
    board = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]
    for command in build_frame:
        x,y, bType, isInsert = command
        if isInsert:
            insert(board, x, y, bType)
        else:
            delete(board, x, y, bType)

    for x, line in enumerate(board):
        for y, element in enumerate(line):
            if element[PILLAR]:
                answer.append([x,y,PILLAR])
            elif element[CROSSBEAM]:
                answer.append([x,y,CROSSBEAM])

    return sorted(answer)

n = 5
frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, frame))
print()

n = 5
frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, frame))
