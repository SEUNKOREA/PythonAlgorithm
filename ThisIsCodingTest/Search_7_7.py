# 집합 자료형 이용
n = int(input())
products = set(map(int, input().split()))

m = int(input())
wants = list(map(int, input().split()))

for want in wants:
    if want in products:
        print('yes', end=' ')
    else:
        print('no', end=' ')