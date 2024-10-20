# 최적화된 스택 - # 1106
# 괄호가 있는 문자열을 파싱하되, 스택에 꼭 필요한 요소만 넣어서 연산
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        # 연산자, 불리언 값, 괄호만 고려한다.
        # 닫는 괄호를 만나면 스택에서 요소를 꺼내서 연산한다.

        stack = []
        for token in expression:
            if token == ')':
                has_true, has_false = False, False
                while stack and stack[-1] not in ['|', '!', '&']:
                    char = stack.pop()
                    if char == 'f':
                        has_false = True
                    if char == 't':
                        has_true = True
                op = stack.pop()  # 연산자 추출
                if op == '|':
                    if has_true:
                        stack.append('t')
                    else:
                        stack.append('f')
                elif op == '&':
                    if has_false:
                        stack.append('f')
                    else:
                        stack.append('t')
                else:
                    if has_true:
                        stack.append('f')
                    else:
                        stack.append('t')

            if token in ['t', 'f', '|', '&', '!']:
                stack.append(token)

        if stack[-1] == 't':
            return True
        else:
            return False
