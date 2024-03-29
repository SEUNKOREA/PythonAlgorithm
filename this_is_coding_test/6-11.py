n = int(input())
data = []

for _ in range(n):
    name, score = input().split()
    data.append((name, int(score)))

# 점수를 기준으로 오름차순 정렬
data.sort(key=lambda x:x[1])

for i in range(n):
    print(data[i][0], end=' ')