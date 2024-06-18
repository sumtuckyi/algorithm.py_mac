class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        new_arr = [(0, 0)] + list(zip(difficulty, profit))  # [(2, 10), (4, 20), ...]
        new_arr.sort()  # tuple 첫번째 요소 기준으로 정렬 => 난이도순
        total = 0  # 출력할 값

        # i번째 난이도의 작업을 할 때 얻을 수 있는 가장 큰 보수를 저장하도록 배열 갱신
        for i in range(len(new_arr) - 1):
            new_arr[i + 1] = (
                new_arr[i + 1][0],
                max(new_arr[i][1], new_arr[i + 1][1])
            )
        # print(new_arr)
        for i in range(len(worker)):
            ability = worker[i]
            # 해당 일꾼이 할 수 있는 일이 없으면 패스
            if ability < new_arr[0][0]:
                continue
            can_do = self.BS(ability, new_arr, len(profit) - 1)
            total += can_do
            # arr = new_arr[:can_do + 1]
            # arr.sort(key=lambda x: x[1])
            # total += arr[-1][1]
            # max_profit = max(j for d, j in new_arr[:can_do + 1])
            # total += max(arr, key=lambda x: x[1])[1]
            # max_profit = 0
            # for i in range(can_do + 1):
            #     max_profit = max(max_profit, new_arr[i][1])
            # total += max_profit

        return total

        # 배열을 이진탐색하여 해당 worker가 수행할 수 있는 난이도의 작업 찾기 & 그 중 가장 높은 보수

    def BS(self, ability, arr, end):  # ability보다 난이도가 낮거나 같아야 함
        s, e = 1, end + 1
        res, job_profit = 0, 0
        while s <= e:
            mid = (s + e) // 2
            if arr[mid][0] <= ability:
                # res = max(res, mid) # 수행할 수 있는 작업 중 가장 큰 인덱스를 저장
                job_profit = max(arr[mid][1], job_profit)
                s = mid + 1
            else:
                e = mid - 1
        # print(job_profit)
        return job_profit


