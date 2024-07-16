# leetcode-1190
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        for token in s:
            if token == '(':
                stack.append(len(res))
            elif token == ')':
                start = stack.pop()
                end = len(res) - 1
                res[start:end+1] = res[start:end+1][::-1]
            else:
                res.append(token)

        return ''.join(res)


class Solution2(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        pair = ['-' for _ in range(len(s))]
        # pair 배열 채우기
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                e = stack.pop()
                pair[e] = i
                pair[i] = e
        res = []
        cur = 0
        dir = True  # True이면 forward, False이면 backward
        while cur < len(s):
            if s[cur] == '(' or s[cur] == ')':
                cur = pair[cur]  # 웜홀로 이동
                dir = not dir  # 탐색 방향을 바꾸기
            else:
                res.append(s[cur])

            if dir:
                cur += 1
            elif not dir:  # 역방향이면
                cur -= 1

        return ''.join(res)
