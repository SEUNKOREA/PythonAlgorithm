from itertools import permutations
def solution(n, weak, dist):
    ## 취약지점 리스트의 길이를 두 배로 늘려서 원형으로 만든다.
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    ## 투입할 친구 수의 최솟값을 찾기위해서 len(dist)+1로 초기화
    answer = len(dist) + 1

    ## 0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        ## 친구를 나열하는 모든 경우의 수 각각에 대해서 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 첫번째 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            # 시작점부터 모든 취약지점을 확인
            for index in range(start, start + length):
                # 첫번째 친구가 점검할 수 있는 마지막 위치보다 취약지점의 값이 더 클 경우
                if position < weak[index]: 
                    count += 1 # 친구 추가
                    # 최대로 추가할 수 있는 친구의 수를 넘어간 경우는 빠져나옴
                    if count > len(dist): 
                        break
                    # 추가한 친구가 점검할 수 있는 마지막 위치 계산
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    return answer



n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

