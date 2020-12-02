def solution(s):
    return True if s.lower().count('p' or 'P') == s.lower().count('y' or 'Y') else True if s.lower().count('p') + s.lower().count('y') == 0 else False
s = "pPoooyY"
print(solution(s))