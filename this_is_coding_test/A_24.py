n = int(input())
data = list(map(int, input().split()))

data.sort()

if len(data) % 2 == 0:
    index = len(data) // 2 -1
else:
    index = len(data) // 2

print(data[index])