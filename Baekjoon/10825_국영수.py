n = int(input())
data = []
for _ in range(n):
    name, kor, eng, mat = input().split()
    data.append([name, int(kor), int(eng), int(mat)])

# 정렬순서: 국어 감소하는 순서, 영어 증가하는 순서, 수학 감소하는 순서, 이름사전순 증가
data.sort(key=lambda x:[x[1]*(-1), x[2], x[3]*(-1), x[0]])

for d in data:
    print(d[0])