exp = '(6+5*(2-8)/2)'
exp2 = '2+3*4/5'
# exp = '2+3*4/5'

'''
입력 받은 중위 표기식에서 토큰을 읽는다.
토근이 연산자이면 토큰을 출력한다. 
토큰이 연산자(괄호 포함)일 때,
만약 스택이 비어있지 않다면
스택의 최상단 값과 비교하여 그보다 우선순위가 높으면 스택에 삽입하고 
그렇지 않다면(우선순위가 동일한 경우도 포함) 토큰의 우선순위가 높을 때까지
스택에서 pop을 반복한 뒤에 토큰을 스택에 삽입한다. 
최상단에 연산자가 없다면 그냥 바로 삽입한다.
만약 토큰이 오른쪽 괄호이면 스택 최상단에 왼쪽 괄호가 올 때까지
pop연산을 수행하고 pop한 연산자를 출력한다. 왼쪽 괄호를 만나면
pop연산만 하고 출력은 하지 않는다.
중위표기식을 다 읽었다면 중지하고 그렇지 않다면 위의 작업을 반복한다.
스택에 남아있는 연산자를 모두 pop하고 출력한다.
'''


operator = ['(', '*', '/', '+', '-']
# value의 숫자가 클수록 우선순위가 높음
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}  # 스택 내에서의 우선순위
stack = []
def to_postfix(exp):
    for i in range(len(exp)):
        if exp[i] in operator:  # 토큰이 연산자라면
            if not stack:  # 스택이 비어있다면
                stack.append(exp[i])  # 해당 연산자를 스택에 삽입
            elif stack and isp[stack[-1]] < icp[exp[i]]:  # 스택 최상단의 연산자의 우선순위가 현재 연산자의 우선순위보다 낮다면
                stack.append(exp[i])  # 현재 연산자를 스택에 삽입
            else:  # 스택 최상단의 연산자의 우선순위가 토큰의 우선순위보다 낮지 않은 경우(크거나 동일)
                while isp[stack[-1]] >= icp[exp[i]]:
                    print(stack.pop(), end=' ')  # 스택 최상단의 연산자를 출력
                stack.append(exp[i])
        elif exp[i] == ')':  # 토큰이 오른쪽 괄호라면
            while stack[-1] != '(':  # 스택 최상단의 값이 '('이 될 때까지
                print(stack.pop(), end=' ')  # 스택 최상단의 값을 출력
            stack.pop()  # 왼쪽 괄호를 스택에서 제거
        else:  # 토큰이 피연산자라면
            print(exp[i], end=' ')  # 출력


def read_exp(exp):
    stack = []
    for i in range(len(exp)):
        if exp[i] not in operator:
            print(exp[i], end=' ')
        else:
            stack.append(exp[i])
    while stack:
        print(stack.pop(), end=' ')

def cal(exp):  # 후위표기식을 입력받아 계산한 뒤 답을 출력
    stack = []
    temp = ''
    for i in range(len(exp)):
        if exp[i] not in operator:
            stack.append(exp[i])
        else:  # 토큰이 연산자인 경우
            temp = stack[-2] + exp[i] + stack[-1]
            for _ in range(2):
                stack.pop()
            stack.append(str(eval(temp)))
            # print(stack)
    print(stack.pop())







to_postfix(exp)
print()
read_exp(exp2)
print()
cal('6528-*2/+')