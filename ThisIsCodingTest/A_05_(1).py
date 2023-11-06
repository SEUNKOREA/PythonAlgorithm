from collections import Counter
n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
info = dict(Counter(data))

value = list(info.values())

result = 0
for i in range(len(value)-1):
    result += value[i] * sum(value[i+1:])
print(result)