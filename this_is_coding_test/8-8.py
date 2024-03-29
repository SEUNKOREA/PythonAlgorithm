# 화폐의 가짓수(n), 목표금액(m)
n, m = map(int, input().split())
# 화폐의 가치 정보 입력받기
coins = [int(input()) for _ in range(n)]

d = [10001] * (m+1)

d[0] = 0 # 0원을 만드는 경우는 화폐를 하나도 사용하지 않았을 때 가능함
for coin in coins:
    for i in range(coin, m+1):
        if d[i - coin] != 10001:
            d[i] = min(d[i], d[i-coin]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])