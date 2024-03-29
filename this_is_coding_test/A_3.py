string = input()

count0 = 0  # 모두 0으로 바꾸는 경우
count1 = 0  # 모두 1로 바꾸는 경우

if string[0] == '0':
    count1 += 1
elif string[0] == '1':
    count0 += 1

for i in range(0, len(string)-1):
    if string[i] != string[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if string[i+1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        elif string[i+1] == '0':
            count1 += 1

print(min(count0, count1))

