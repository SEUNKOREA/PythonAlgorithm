from collections import Counter

# 배열의 길이와 찾고자 하는 숫자 입력받기
n, x = list(map(int, input().split(' ')))
# 정렬된 배열 입력받기
array = list(map(int, input().split()))

info = dict(Counter(array))

if x not in info:
    print(-1)
else:
    print(info[x])