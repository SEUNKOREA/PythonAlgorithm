def dfs(x, y):


n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]

init_x, init_y = 0, 0
for i in range(n):
    for j in range(m):
        dfs(i, j)