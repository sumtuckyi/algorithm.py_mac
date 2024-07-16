# leetcode - 726
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        :type formula: str
        :rtype: str
        """
        n = len(formula)
        stack = [defaultdict(int)]

        index = 0

        # 전체 문자열 선형 탐색
        while index < n:
            # 여는 괄호가 나오면 새 딕셔너리를 스택에 삽입.
            # 이 새 딕셔너리는 중첩된 식의 원자 수를 카운트 해서 저장할 딕셔너리
            if formula[index] == '(':
                stack.append(defaultdict(int))
                index += 1

            # 닫는 괄호가 나오면 스택 최상단에서 딕셔너리를 반환
            # 중첩된 식이 끝날 때, 계산이 필요
            elif formula[index] == ')':
                cur_map = stack.pop()  # 중첩식을 처리할 것
                index += 1
                mtp = ""
                # 숫자가 끝날 때까지 추적 - mtp값을 찾는 과정
                while index < n and formula[index].isdigit():
                    mtp += formula[index]
                    index += 1
                if mtp:  # 연이어 숫자가 오는 경우 - 아니라면 1이 곱해질 것
                    mtp = int(mtp)  # 문자열을 정수로 변환
                    for atom in cur_map:  # 닫히는 괄호 안에 있는 원자에만 값을 곱해줌
                        cur_map[atom] *= mtp

                # 전체 원자 수 딕셔너리에 중첩된 식의 원자 수 더해주기 -> 이로써 괄호 안의 수식 처리 완료
                for atom in cur_map:
                    stack[-1][atom] += cur_map[atom]

            # 새로운 원자 등장 - 대문자인 경우
            else:
                cur_atom = formula[index]
                index += 1
                # 소문자가 아닐때까지 추적 - 새로운 원소 이름을 찾는 과정
                while index < n and formula[index].islower():
                    cur_atom += formula[index]
                    index += 1

                # 새로운 원소를 찾았으므로 원자의 숫자 찾기
                cur_cnt = ""
                while index < n and formula[index].isdigit():
                    cur_cnt += formula[index]
                    index += 1

                if cur_cnt == "":  # 1이어서 원자이름 뒤 숫자가 생략된 경우라면
                    stack[-1][cur_atom] += 1
                else:
                    stack[-1][cur_atom] += int(cur_cnt)

        # 딕셔너리를 알파벳 순으로 정렬
        final_map = dict(sorted(stack[0].items()))

        ans = ""
        for atom in final_map:
            ans += atom  # 키 값 더하기
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans









