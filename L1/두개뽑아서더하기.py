def solution(numbers):
    answer = []

    k = set()
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            k.add(numbers[i] + numbers[j])
    
    answer = list(k)
    answer.sort()
    return answer

#numbers = list(map(int,input().split()))
numbers = [1,1,1,1,1]
print(solution(numbers))