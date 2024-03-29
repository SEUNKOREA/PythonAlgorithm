n, k = map(int, input().split())

cnt = 0

while True:
    # 가장 가까운 k배수까지 한 번에 빼기
    nearest = (n // k) * k
    n = nearest
    cnt += (n - nearest)

    # k보다 작은지 체크
    if n < k:
        break

    # k보다 크다면 k로 나눠준다
    n //= k
    cnt += 1

# 1까지 빼기
cnt += (n-1)
print(cnt)