# 계수정렬 소스코드

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array)+1)

# array의 모든 원소를 순회하면서 해당하는 count 리스트의 값을 1씩 증가시킴
for i in array:
    count[i] += 1

# count 리스트에 저장된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')