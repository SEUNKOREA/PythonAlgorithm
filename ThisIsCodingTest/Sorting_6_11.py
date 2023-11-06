n = int(input())

data = []
for _ in range(n):
    name, score = input().split()
    data.append((name, int(score)))

data = sorted(data, key=lambda x: x[1])

for i in range(len(data)):
    print(data[i][0], end=' ')