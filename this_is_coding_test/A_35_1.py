import heapq

n = int(input())

array = []

heap = []
heapq.heappush(heap,1)

while len(array) < n:
    now = heapq.heappop(heap)
    for i in [2, 3, 5]:
        temp = now * i
        if temp not in heap:
            heapq.heappush(heap, temp)
    array.append(now)

print(array[n-1])
