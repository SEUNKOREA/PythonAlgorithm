def check(p):
    stack = [] # 괄호가 임시로 저장될 스택

    for idx, chr in enumerate(p):
        # 괄호쌍 맞는지 체크
        if idx == 0:
            stack.append(chr)
        else:
            if len(stack) == 0:
                stack.append(chr)
            else:
                pre = stack.pop()
                if pre == "(" and chr == ")":
                    continue
                else:
                    stack.append(pre)
                    stack.append(chr)
    if len(stack) == 0:
        str_type = "correct"
    else:
        str_type = "balanced"
    return str_type

def split_u_v(p):
    left, right = 0, 0
    u, v = "", ""
    flag = False

    for idx, chr in enumerate(p):
        if chr == "(": left += 1
        else: right += 1
        u += chr

        if left == right: 
            v = p[idx+1:]
            break
    return u, v

def transform(w):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if w == '':
        return ''
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, 
    # v는 빈 문자열이 될 수 있습니다. 
    u, v = split_u_v(w)
    # print(f"u: {u}, v: {v}")

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if check(u) == 'correct':
        v_tr = transform(v)
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        # print(f"v_tr: {v_tr}") 
        return u + v_tr
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
    temp = "("
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    v_tr = transform(v)
    temp += v_tr
    # 4-3. ')'를 다시 붙입니다. 
    temp += ")"
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고,
    u = u[1:-1]
    #  나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    for uu in u:
        if uu == "(": temp += ")"
        elif uu == ")": temp += "("
    # 4-5. 생성된 문자열을 반환합니다.
    return temp

def solution(p):
    if check(p) == 'correct':
        return p
    else:
        return(transform(p))


p_s = ["(()())()", ")(", "()))((()"]

for p in p_s:
    print(solution(p))