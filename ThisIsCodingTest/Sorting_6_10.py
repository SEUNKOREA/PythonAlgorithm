# 위에서 아래로

# 내 풀이
n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)
for d in data:
    print(d,end=' ')

# 모범답안
# 모든 수가 1 이상 100,000이하이므로 어떠한 정렬 알고리즘을 사용해도 문제를 해결할 수 있지만
# 코드가 가장 간단한 파이썬의 기본 정렬 라이브러리를 사용하는 것이 효과적이다.
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end= ' ')