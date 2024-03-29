# 계수정렬을 이용한 풀이
n = int(input())
stock = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

dp = [0] * (max(stock)+1)
for stock_num in stock:
    dp[stock_num] += 1

for request_num in request:
    if dp[request_num] != 0:
        print("yes", end=' ')
    else:
        print("no", end=' ')