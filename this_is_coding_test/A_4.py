n = int(input())
coins = list(map(int, input().split()))

# 가지고 있는 동전을 오름차순 정렬
coins.sort()

target = 1
for coin in coins:
    # 만들 수 없는 금액을 찾았을 때 반복종료
    if target < coin:
        break
    target += coin

print(target)