n, m = map(int, input().split())
data = list(map(int, input().split()))

weight = [0] * (m+1)

for d in data:
    weight[d] += 1

result = 0

for i in range(1, m):
    n -= weight[i]
    result += weight[i] * n
    
print(result)
