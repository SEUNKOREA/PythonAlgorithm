"""
이코테 그리디 실전4. 1이 될 때까지
"""
# 단순하게 푸는 답안 예시
# n의 범위가 늘어나면 시간초과가 뜰 수 있음
n, k = map(int, input().split())
answer = 0

while n >= k:
    while n % k != 0:
        n -= 1
        answer += 1
    n //= k
    answer += 1

while n > 1:
    n -= 1
    answer += 1

print(answer)