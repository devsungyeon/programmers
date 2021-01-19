def ternary(n):
    li = []
    while n != 0:
        li.append(n%3)
        n //= 3
    return li

def solution(n):
    answer = 0
    li = ternary(n)
    li.reverse()
    for i in range(len(li)):
        answer += li[i]*(3**i)
    return answer

print(solution(int(input())))