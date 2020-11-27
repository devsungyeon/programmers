import datetime

def solution(a, b):
    answer = ''
    y = 2016
    li = ["SUN", "MON","TUE","WED","THU","FRI","SAT"]
    print(datetime.date(y,a,b).weekday())
    answer = li[(datetime.date(y,a,b).weekday()+1)%7]
    return answer

m, d = map(int, input().split())
print(solution(m, d))