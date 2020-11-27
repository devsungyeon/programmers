def solution(board, moves):
    answer = 0
    board.reverse()
    board = list(map(list, zip(*board)))
    
    li = []
    for tli in board:
        tmp = []
        for i in tli:
            if i == 0:
                break
            tmp.append(i)
        li.append(tmp)
    
    ans = []
    for i in moves:
        if ans:
            a = ans.pop()
            if li[i-1]:
                b = li[i-1].pop()
                if a == b:
                    answer += 2
                else:
                    ans.append(a)
                    ans.append(b)
            else:
                ans.append(a)
        else:
            if li[i-1]:
                ans.append(li[i-1].pop())

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))