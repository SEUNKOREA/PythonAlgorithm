"""
BOJ 15649 N과 M(1)
출처: https://www.acmicpc.net/problem/15649
"""
def dfs(alst):
    # 종료조건: 정답 리스트의 길이가 M이라면 수배열 반환
    if len(alst) == M:
        print(*alst)
        return
    # 하부함수 호출
    # 1 ~ N까지의 수 중에서 수배열에 포함되지 않은 경우
    # 그 수를 정답리스트에 추가하여 하부함수 호출
    for i in range(1, N+1):
        if i not in alst:
            alst.append(i)
            dfs(alst)
            alst.pop()

N, M = map(int, input().split())
dfs([])
