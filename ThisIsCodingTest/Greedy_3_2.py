# 큰 수의 법칙
n, m, k = map(int, input().split()) # m: 총 횟수, k: 최대반복횟수
data = list(map(int, input().split()))

result = 0

data.sort()
first = data[-1]
second = data[-2]

q = m // (k+1)
r = m % (k+1)

answer = q * (k * first + second) + r * first

print(answer)