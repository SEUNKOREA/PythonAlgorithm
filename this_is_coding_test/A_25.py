def solution(N, stages):
    num = len(stages)
    fail = []
    for stage in range(1, N+1):
        not_solved = stages.count(stage)
        if num == 0:
            failure = 0
        else:
            failure = not_solved / num
        
        fail.append((stage, failure))
        num -= not_solved

    fail.sort(key=lambda x:(-x[1], x[0]))

    answer = [f[0] for f in fail]
    return answer