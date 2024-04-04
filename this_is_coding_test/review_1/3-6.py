"""
이코테 그리디 실전4. 1이 될 때까지
"""
n, k = map(int, input().split())
answer = 0
while True:
    target = k * (n // k)
    answer += (n - target)
    n = target
    if n < k:
        break
    n //= k
    answer += 1

answer += (n-1)
print(answer)