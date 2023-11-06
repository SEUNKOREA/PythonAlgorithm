import sys

n = int(input())
btwn_len = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

answer = cost[0] * btwn_len[0]
min_cost = cost[0]

for i in range(1, n-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    answer += min_cost * btwn_len[i]

print(answer)
