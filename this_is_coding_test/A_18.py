def check_right(p):
    temp = []

    for i in range(len(p)):
        if p[i] == "(":
            temp.append(p[i])
        else:
            if len(temp) == 0:
                return False
            if temp[-1] == "(":
                temp.pop()
    
    if len(temp) == 0:
        return True

def split_u_v(p):
    cnt_left = 0
    cnt_right = 0

    u = ""
    v = ""
    
    for i in range(len(p)):
        if p[i] == "(":
            cnt_left += 1
        else:
            cnt_right += 1
        
        if cnt_left == cnt_right:
            u = p[:i+1]
            v = p[i+1:]
            return u, v


def solution(p):
    if p == "":
        return p
    
    u, v = split_u_v(p)

    if check_right(u):
        answer = u + solution(v)
        return answer
    
    else:
        answer = ""
        answer += "("
        answer += solution(v)
        answer += ")"
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == "(":
                answer += ")"
            else:
                answer += "("
        return answer
