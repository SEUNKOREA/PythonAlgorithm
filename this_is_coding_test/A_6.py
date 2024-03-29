import heapq
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 적게 걸리는 음식부터 빼야하므로 우선순위 큐를 이용
    q = []
    for idx, food_time in enumerate(food_times):
        # (음식을 먹는데 걸리는 시간, 음식번호)로 우선순위 큐 삽입
        heapq.heappush((food_time, idx+1))
    
    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전에 다 먹은 음식 시간
    previous = 0
    # 남은 음식의 개수
    length = len(food_time)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다먹은 음식 제외
        previous = now # 이전음식시간 재설정

    # 남은 음식 중에서 몇번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x:x[1])
    return result[(k-sum_value) % length][1]


solution(food_times=[3, 1, 2], k=5)
