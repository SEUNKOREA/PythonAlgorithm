n = int (input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0

a.sort() # 오름차순 0,1,1,1,6

for aa in a:
    answer += aa * max(b)
    b.pop(b.index(max(b)))
print(answer)