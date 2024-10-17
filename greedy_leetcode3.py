# 670
from collections import defaultdict


class Solution:
    def maximumSwap(self, num: int) -> int:

        if num == 0:
            return num

        else:
            table = defaultdict(int)
            num_arr = [int(x) for x in str(num)]  # 정수인 요소를 가진 순회가능한 객체로 만들어줌

            new_set = set(num_arr)  # 중복제거
            new_set = sorted(new_set, reverse=True)  # 내림차순 정렬
            rank = 1
            for digit in new_set:  # 우선순위 정보 저장하기
                table[digit] = rank
                rank += 1

            priority = []
            # num의 자릿수별 우선순위 계산하기
            for digit in num_arr:
                priority.append(table[digit])
            # print(priority)
            # swap할 숫자의 자릿수 저장하기
            left, right = 0, 0
            tof = False
            for i in range(len(priority)):  # left 정하기 - 정렬이 안 된 구간의 시작점을 찾아야함..
                # p 값을 기준으로 i + 1 이후의 위치에 p보다 우선순위가 높은 수가 있으면 그 수와 바꾼다.
                # 단 그 중에서도 가장 뒤에 있으면서 우선순위가 높은 수와 바꾼다.
                MAX = priority[i]  # 이거보단 낮아야함
                for j in range(len(priority) - 1, i, -1):  # i보다 큰 인덱스의 우선순위와 뒤에서부터 비교
                    if priority[j] < priority[i]:
                        if priority[j] < MAX:  # 기존에 나온 우선순위보다도 더 낮은 경우
                            MAX = priority[j]
                            right = j
                if MAX != priority[i]:  # 한 번이라도 값의 갱신이 있었다면
                    left = i
                    break
                    # print(left, right)

            if left != right:  # swap하기
                temp = num_arr[left]
                num_arr[left] = num_arr[right]
                num_arr[right] = temp

            return int(''.join([str(x) for x in num_arr]))


