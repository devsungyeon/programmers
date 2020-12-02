def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    answer = participant[len(participant)-1]
    for i in range(0,len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]    
            break
        
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))