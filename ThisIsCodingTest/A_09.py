def solution(s):
    length = len(s)
    answer = length  # 초기값은 문자열 전체 길이

    for step in range(1, length // 2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1

        for i in range(step, length, step):
            current = s[i:i + step]

            if prev == current:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = current
                count = 1

        compressed += str(count) + prev if count > 1 else prev
        compressed += s[i + step:]

        answer = min(answer, len(compressed))

    return answer