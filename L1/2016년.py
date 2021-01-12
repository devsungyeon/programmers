import sys
import datetime

a,b = map(int, input().split())
weekdays = ['SUN','MON','TUE','WED','THU','FRI','SAT']
monthdays = [0,31,29,31,30,31,30,31,31,30,31,30,31]
print(weekdays[(sum(monthdays[:a])+b+4)%7])