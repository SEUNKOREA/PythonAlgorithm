n, k = map(int, input().split())

cnt = 0

# n이 k이상이면 계속 나누기
while n >= k:
    # 나눠떨어질때까지 계속 1 빼기
    while n % k != 0:
        n -= 1
        cnt += 1
    # k로 나누기
    n //= k
    cnt += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    cnt += 1

print(cnt)