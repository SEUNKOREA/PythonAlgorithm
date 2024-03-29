import heapq

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

answer = 0

while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    answer += sum_value
    heapq.heappush(heap, sum_value)

print(answer)