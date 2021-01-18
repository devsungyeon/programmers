def sumfromone(q):
    return int((q**2+q)/2)

def solution(a, b):
    answer = 0
    if a == b:
        return a
    answer = sumfromone(max(a,b)) - sumfromone(min(a,b)-1)
    return answer

a = int(input())
b = int(input())
print(solution(a,b))