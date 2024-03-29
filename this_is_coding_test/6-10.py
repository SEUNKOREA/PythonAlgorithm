n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)
for i in range(n):
    print(data[i], end=' ')