
num = int(input())
ls = []
for i in range(num): 
    ls.append(input())

def recursive(st):
    cnt = 0
    while cnt < 26:
        st = st.replace('()', '')
        cnt += 1
    return st


for st in ls:
    if len(st) % 2 == 0 and recursive(st) == '' :
        print('YES')
    else :
        print('NO')



#풀이 - 스택 이용하기
#먼저 들어오는 여는 괄호는 나중에 들어오는 닫는 괄호와 매칭이 됨
#처음의 닫는 괄호와 가장 인접한 괄호와 매칭됨
#stack에 첫번째 여는 괄호, 두번째 여는 괄호, 세번째 여는 괄호를 순서대로 입력
#stack에 다음으로 닫는 괄호가 들어왔을 때 세번째 여는 괄호가 삭제됨

#stack을 사용한 내 풀이
num = int(input())
ls = []
for _ in range(num): 
    ls.append(list(input()))

for st_list in ls:
    stack = []
    for i in st_list:
        if i == '(':
            stack.append(i)
        else: #i == ')'
            if len(stack) > 0 and stack[-1] == '(':
                a = stack.pop()
            else:
                stack.append(i) #i == ')'인 경우에도 stack에 저장해야함

    if stack == []:
        print('YES')
    else:
        print('NO')

#강의 풀이
for _ in range(int(input())):
    stk = [] #스택 생성
    isVPS = True
    for ch in input(): 
        if ch == '(':
            stk.append(ch)
        else :
            if stk: #stack이 비어있지 않은 경우 pop
                stk.pop()
            else:
                isVPS = False
                break
    
    if stk: #최종 stack이 비어있지 않는 경우
        isVPS = False
    

    print('YES' if isVPS else 'NO')