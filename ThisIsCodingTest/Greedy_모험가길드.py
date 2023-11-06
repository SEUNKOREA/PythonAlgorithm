# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 떠날 수 있음
# 최대 몇 개의 모험가 그룹을 만들 수 있는지
# 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램

# 그룹 1에 공포도가 1,2,3인 모험가를 한 명씩 넣고
# 그룹 2에 공포도가 2인 남은 두 명을 넣게 되면
# 최종적으로 2개의 그룹을 만들 수 있습니다.
# 몇 명의 모험가는 마을에 그대로 남아있어도 되기 때문에
# 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.

n = int(input()) # 5
data = list(map(int, input().split())) # [2, 3, 1, 2, 2]
data.sort() # [1, 2, 2, 2, 3]

result = 0  # 총 그룹의수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:      # 공포도를 낮은 것부터 하나씩 확인하면서
    count += 1      # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0   # 현재 그룹에 포함된 모험가의 수 초기화

print(result)




     
