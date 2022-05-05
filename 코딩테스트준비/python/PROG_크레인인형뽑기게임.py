board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    bag = list()

    for n in moves:

        n -= 1
        for a in range(len(board[n])):


            # 0이 아닌 인형이면
            if board[a][n] != 0:

                if not bag:
                    bag.append(board[a][n])
                    board[a][n] = 0
                    break

                if bag[-1] == board[a][n]:
                    answer +=2
                    bag.pop()
                else:
                    bag.append(board[a][n])
                board[a][n] = 0
                break





    return answer

solution(board, moves)