def solution(n):
    answer = ''
    half = n // 2
    remain = n - half * 2
    answer = "수박" * half
    answer += "수"*remain
    return answer

n = int(input())
print(solution(n))