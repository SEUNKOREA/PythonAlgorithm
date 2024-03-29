n = int(input())
result = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            time = str(hour) + str(minute) + str(second)
            if '3' in time:
                result += 1

print(result)