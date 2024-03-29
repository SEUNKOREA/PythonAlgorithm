"""
코드트리 오마카세
출처: https://www.codetree.ai/training-field/frequent-problems/problems/codetree-omakase/description?page=1&pageSize=20
"""

class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

# 명령집합
queries = []

# 등장한 사람 목록
names = set()

# 각 사람마다 주어진 초밥 명령
p_queries = {}

# 각 사람마다 입장시간
entry_time = {}

# 각 손님의 위치
position = {}

# 각 사람마다 퇴장시간
exit_time = {}

# Query를 (t, cmd) 순으로 정렬
# 시간이 같은 경우 명령수행 순서 100 -> 200 -> 300
def cmp(q1, q2):
    if q1.t == q2.t:
        return q1.t < q2.t
    return q1.cmd < q2.cmd

# 입력
L, Q = map(int, input().split())
for _ in range(Q):
    # 입력받은 명령을 각 수행명령에 따라 입력처리
    command = input().split()
    cmd, t, x, n = -1, -1, -1, -1 # 각 명령에 없는 값들은 -1로 설정
    name = ""
    cmd = int(command[0])
    if cmd == 100:
        t, x, name = command[1:]
        t, x = map(int, [t, x])
    elif cmd == 200:
        t, x, name, n = command[1:]
        t, x, n = map(int, [t, x, n])
    else:
        t = int(command[1])

    # 입력처리한 명령들을 묶어서 클래스로 관리
    queries.append(Query(cmd, t, x, name, n))

    # 사람이름으로 초밥을 먹게 되기 때문에 초밥이 생성되면 그 초밥은 무조건 그 사람이 먹어야하므로
    # 사람별로 주어진 초밥목록을 관리한다.
    if cmd == 100:
        if name not in p_queries:
            p_queries[name] = []
        p_queries[name].append(Query(cmd, t, x, name, n))
    # 손님이 입장한 시간과 위치를 관리한다.
    elif cmd == 200:
        names.add(name)
        entry_time[name] = t
        position[name] = x

# 각 사람마다 자신의 이름이 적힌 초밥을 언제 먹게 되는지 계산
for name in names:
    # 해당 사람의 퇴장 시간을 관리한다.
    exit_time[name] = 0

    # 각 사람에게 주어진 초밥들을 확인
    for q in p_queries[name]:
        time_to_removed = 0 # 초밥이 사라지는 시간을 계산
        if q.t < entry_time[name]:
            # 아직 입장하기 전에 자신의 이름이 적힌 초밥이 만들어졌다면
            # 입장했을 때 그 스시는 어디에 있는지 구한다.
            t_sushi_x = (q.x + (entry_time[name] - q.t)) % L
            # 입장했을 때 스시의 위치와 그 사람이 입장했을 때 위치값을 빼면
            # 몇 초가 지나야 그 사람에게 도달하는지 계산 가능
            additional_time = (position[name] - t_sushi_x + L) % L
            # 초밥이 지워지는 시간은 고객이 입장하고 나서 그 초밥이 고객에게 도달한 시간을 더한 값
            time_to_removed = entry_time[name] + additional_time
        else: # 사람이 입장한 후에 초밥이 주어졌다면
            additional_time = (position[name] - q.x + L) % L
            # 초밥이 지워지는 시간은 초밥이 생성되고 고객에게 도달한 시간
            time_to_removed = q.t + additional_time

        # 가장 마지막 초밥이 사라지는 시간이 곧 그 사람의 퇴장시간
        # 초밥이 사라지는 시간 중 가장 늦은 시간을 업데이트
        exit_time[name] = max(exit_time[name], time_to_removed)

        # 초밥이 사라지는 111번 쿼리를 추가
        queries.append(Query(111, time_to_removed, -1, name, -1))

# 사람마다 초밥을 마지막으로 먹은 시간을 계산해서 그 사람이 해당 시간에 매장을 떠났다는 쿼리를 추가
for name in names:
    queries.append(Query(222, exit_time[name], -1, name, -1))

# 전체 Query를 시간순으로 정렬
# 이 때 t가 일치한다면 100 > 111 > 200 > 222 > 300순으로 정렬되도록
queries.sort(key=lambda q: (q.t, q.cmd))

people_num, sushi_num = 0, 0
for i in range(len(queries)):
    if queries[i].cmd == 100:
        sushi_num += 1
    elif queries[i].cmd == 111:
        sushi_num -= 1
    elif queries[i].cmd == 200:
        people_num += 1
    elif queries[i].cmd == 222:
        people_num -= 1
    else:
        print(people_num, sushi_num)