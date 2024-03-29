string = input()

answer = int(string[0])

for s in string[1:]:
    if answer == 0 or int(s) == 0:
        answer += int(s)
    else:
        answer *= int(s)

print(answer)
