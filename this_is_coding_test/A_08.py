string = input()
result = []
sum = 0
exist_num = False
for s in string:
    if s.isalpha():
        result.append(s)
    else:
        sum += int(s)
        exist_num = True
result.sort()
if exist_num:
    result.append(str(sum))
print(''.join(result))


