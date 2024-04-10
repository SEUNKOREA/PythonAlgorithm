"""
BOJ 1697. 숨바꼭질
출처: https://www.acmicpc.net/problem/1697
"""

### BFS를 이용한 풀이
def bfs(start, end):
    q = []
    visited = [0] * 200001

    q.append(start)
    visited[start] = 1

    while q:
        c = q.pop(0)
        if c == end:
            return visited[end] - 1
        for nc in [c-1, c+1, 2*c]:
            if 0 <= nc <= 200000 and not visited[nc]:
                q.append(nc)
                visited[nc] = visited[c] + 1

N, K = map(int, input().split())
ans = bfs(N, K)
print(ans)




