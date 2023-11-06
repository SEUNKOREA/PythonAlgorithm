# 숫자카드 게임
n, m = map(int, input().split()) # n:행, m:열
matrix = [list(map(int, input().split())) for _ in range(n)]

sorted_matrix = [sorted(row) for row in matrix]
sorted_matrix.sort(key=lambda x: x[0])

print(sorted_matrix[n-1][0])