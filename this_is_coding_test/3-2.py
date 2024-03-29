n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

answer = 0

num_list.sort()
first = num_list[-1]
second = num_list[-2]

# 가장 큰 수가 더해지는 횟수
first_num = (m // (k+1)) * k
first_num += m % (k+1)

# 두번째 큰 수가 더해지는 횟수
second_num = m // (k+1)

# 정답
answer += (first * first_num) + (second * second_num)
print(answer)