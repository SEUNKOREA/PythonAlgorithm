"""
왼쪽과 오른쪽으로 창문을 열었을 때,
양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다

"""

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    n = int(input()) # 건물의 개수
    array = list(map(int, input().split())) # 건물의 높이가 담긴 리스트

    answer = 0  # 조망권이 확보된 세대의 수

    for i in range(2, n-2):
        left_1 = array[i] - array[i-2]
        left_2 = array[i] - array[i-1]
        right_1 = array[i] - array[i+1]
        right_2 = array[i] - array[i+2]

        if left_1 > 0 and left_2 > 0 and right_1 > 0 and right_2 > 0:
            answer += min(left_1, left_2, right_1, right_2)

    print(f"#{tc} {answer}")