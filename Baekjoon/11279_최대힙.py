import heapq
import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    num = int(sys.stdin.readline())
    # x가 자연수라면 배열에 x라는 값을 추가
    if num > 0:
        heapq.heappush(num_list, -num)
    # x가 0이라면 배열에서 가장 큰 값 출력
    elif num == 0:
        if len(num_list) == 0:
            print(0)
        else:
            print(-heapq.heappop(num_list))
    #print(f"current: {num_list}")