# 백트래킹으로 부분집합을 구하되(조합), 부분집합이 중복되지 않도록 부분집합 생성시에 걸러낸다.(중복없는 조합)- 40
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        candidates.sort()  # 중복제거를 위한 정렬

        cases = []

        # 부분집합을 만들면서 target에서 candidates[i]를 빼는 방식으로 전개
        def backtrack(start, target, path):
            print(start, path)
            if target == 0:  # 목표값을 채운 경우
                cases.append(path[:])
                return
            if target < 0:  # 목표값을 초과한 경우
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # 같은 레벨에서 중복된 숫자 건너뛰기
                if candidates[i] > target:
                    break  # 현재 숫자가 목표보다 크면 더 이상 진행할 필요 없음

                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return cases

sol = Solution()
arr = [1,2,3]
print(sol.combinationSum2(arr, 30))