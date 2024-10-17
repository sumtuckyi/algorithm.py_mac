# 우선순위큐, 최대힙으로 사용하기 + 그리디 - #1405
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        pq = [x for x in pq if x[0] < 0] # 0개인 문자는 제거
        heapq.heapify(pq)
        ans = []

        while pq:
            first = heapq.heappop(pq)  #가장 큰 문자를 꺼낸다.
            # print(first)
            if len(ans) >= 2:
                if ans[-2] == ans[-1] == first[1]:  # 세 개의 문자가 연속해서 오게 되는 경우라면
                    if len(pq):  # 최대힙에 남은 문자가 있는 경우에
                        second = heapq.heappop(pq)
                        ans.append(second[1])
                        if second[0] + 1 != 0: # 1개를 사용하고도 아직 문자가 남았다면
                            heapq.heappush(pq, [second[0] + 1, second[1]])
                        heapq.heappush(pq, [first[0], first[1]]) # 2개 연속으로 붙은 이 문자는 이번 턴에 사용하지 않음. 그대로 다시 힙으로
                    else: # 남은 문자가 없다면
                        break # 반복문 종료
                else: # 세 개의 문자가 연속하지 않는다면
                    ans.append(first[1]) # 문자를 이어붙이고
                    if first[0] + 1 != 0: # 남은 문자가 있다면
                        heapq.heappush(pq, [first[0] + 1, first[1]])
            else: # 이어붙인 문자열의 길이가 1이하라면 같은지 무조건 이어붙일 수 있음
                ans.append(first[1]) # 문자를 이어붙이고
                if first[0] + 1 != 0: # 남은 문자가 있다면
                    heapq.heappush(pq, [first[0] + 1, first[1]])
                    # print(pq)


        return ''.join(ans)