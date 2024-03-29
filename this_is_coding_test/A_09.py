def solution(s):
    length = len(s)
    prev = ''
    result = len(s)

    for interval in range(1, length//2+1):
        string = ''
        for i in range(0, length, interval):
            if i == 0:
                prev = s[i: i+interval]
                cnt = 1
            else:
                part = s[i: i+interval]
                if prev == part:
                    cnt += 1
                else:
                    if cnt == 1:
                        string += prev
                    else:
                        string += str(cnt) + prev
                    prev = part
                    cnt = 1
        if cnt == 1:
            string += prev
        else:
            string += str(cnt) + prev
        result = min(result, len(string))
        
    return result
