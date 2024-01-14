import sys

n, c = map(int, sys.stdin.readline().split())
array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

"""
IDEA
인접한 두 공유기 사이의 거리를 찾을 때
가능한 최소거리부터 가능한 최대거리까지 순차적으로 찾는 것이 아니라
이진탐색을 이용해서 최소거리와 최대거리의 mid 값으로 인접한 두 공유기 사이의 거리를 설정하고
실제로 공유기를 설치해보고 가능하다면 거리를 점차 늘리고 불가능하다면 거리를 점차 줄이는 방식
"""

array.sort()

start = 1                  # 가능한 최소거리
end = array[-1] - array[0] # 가능한 최대거리
result = 0                 # 출력할 

while start <= end:
    mid = (start + end) // 2    # mid값으로 인접한 두 공유기 사이 거리 설정

    value = array[0]            # 실제 공유기 설치를 진행할 때 시작점이 될 지점
    count = 1                   # 시작점에는 공유기를 설치한다고 가정하므로 count의 defalt는 1

    # 현재의 mid값을 이용해 공유기 설치 시뮬레이션 start
    for i in range(1, n):
        if array[i] >= value + mid: # 기준점 위치에서부터 mid 간격 이상에 집이 있으면 공유기 설치
            value = array[i]        # 기준점 위치 업데이트
            count += 1              # 설치된 공유기 개수 업데이트
        else:                       # 기준점 위치에서부터 mid 간격 미만이면 공유기 설치 못함
            pass
    
    # 시뮬레이션 돌렸을 때 
    if count >= c:       # 설치된 공유기의 개수가 설치해야하는 공유기의 개수보다 많거나 같으면
        start = mid + 1  # start 지점을 늘려서 간격을 늘려본다
        result = mid     # 중간 간격값 저장
    else:                # 설치된 공유기의 개수가 설치해야하는 공유기의 개수보다 작으면
        end = mid - 1    # end 지점을 이동시켜서 간격을 줄인다

# 이진탐색으로 정답을 탐색하기 떄문에 결과는 Result 단순출력으로 ok
print(result)