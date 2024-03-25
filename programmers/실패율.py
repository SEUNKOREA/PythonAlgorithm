def solution(N, stages):
    num_challengers = len(stages)
    answer = []

    for current_stage in range(1, N+1):
        count = 0
        for stage in stages:
            if current_stage == stage:
                count += 1
        
        if num_challengers == 0:
            fail = 0
        else:
            fail = count / num_challengers
        
        answer.append((current_stage, fail))

        num_challengers -= count
    
    answer.sort(key= lambda x:x[1], reverse=True)
    return [a[0] for a in answer]
    
    

print(solution(N=5, stages=[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(N=4, stages=[4, 4, 4, 4, 4]))