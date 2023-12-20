import sys

s = sys.stdin.readline().rstrip() # 길이 1이상 49이하
t = sys.stdin.readline().rstrip() # 길이 2이상 50이하
# t의 길이가 항상 s의 길이보다 길다

# 문자열 뒤에 A를 추가한다.
# 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
# s를 t로 바꿀 수 있으면 1, 없으면 0

def check(t):
    if t == s:
        return 1
    if len(s) >= len(t):
        return 0
    
    answer = 0
    if t[-1] == 'A':
        answer = check(t[:-1])
    
    if answer == 1:
        return 1
    
    if t[0] == 'B':
        answer = check(t[1:][::-1])
    
    return answer

answer = check(t)
print(answer)