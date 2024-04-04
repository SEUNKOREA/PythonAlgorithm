"""
이코테 그리디 실전2. 큰 수의 법칙
"""
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first_max = data[-1]
second_max = data[-2]
sum_value = first_max * k + second_max

answer = sum_value * (m // (k+1)) + first_max * (m % (k+1))
print(answer)