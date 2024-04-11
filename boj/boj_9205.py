"""
BOJ 9205. 맥주 마시면서 걸어가기
출처: https://www.acmicpc.net/problem/9205
"""
import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(si, sj, ei, ej):
    q = deque()
    v = [0] * n

    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        if abs(ci-ei) + abs(cj-ej) <= 1000:
            return "happy"
        # 미방문한 모든 편의점좌표에서: 범위내인지 체크
        for i in range(n):
            if v[i] == 0: # 미방문 편의점
                ni, nj = lst[i]
                if abs(ci-ni) + abs(cj-nj) <= 1000: # 범위 내
                    q.append((ni, nj))
                    v[i] = 1
    return "sad"

t = int(input())
for tc in range(t):
    ### 입력받기
    n = int(input())                    # 편의점개수
    si, sj = map(int, input().split())  # 상근이네 집 좌표
    lst = [tuple(map(int, input().split())) for _ in range(n)]     # 편의점 좌표
    ei, ej = map(int, input().split())  # 락 페스티벌 좌표

    ans = bfs(si, sj, ei, ej)
    print(ans)


