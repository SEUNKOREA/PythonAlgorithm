import heapq

n = int(input())
data = [int(input()) for _ in range(n)]
heapq.heapify(data)

answer = 0

while len(data) >= 2:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    answer += (a+b)
    heapq.heappush(data, a+b)

print(answer)