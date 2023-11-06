n = [int(nn) for nn in input()]

n.sort(reverse=True) # 오름차순
answer = -1
if (n[-1] == 0) & (sum(n)%3 == 0):
    answer = int(''.join([str(nn) for nn in n]))

print(answer)