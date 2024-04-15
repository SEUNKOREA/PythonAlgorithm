import sys
sys.stdin = open('input.txt', 'r')
def dfs(n, sm):
    # [1] 종료조건: 현재 확인하는 날짜가 종료일 이후인 경우
    if n == N+1:
        global ans
        ans = max(ans, sm)
        return
    # [2] 하부함수 호출
    # [2-1] 상담을 진행하는 경우
    if n + T[n] <= N: # 다음 상담진행날짜가 N 보다 작거나 같은 경우
        dfs(n + T[n], sm + P[n])
    dfs(n+1, sm)



N = int(input())

T = [0] * (N+1)
P = [0] * (N+1)
for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)