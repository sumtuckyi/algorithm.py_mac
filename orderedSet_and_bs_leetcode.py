# 데이터의 정렬 상태 유지 및, 이진 탐색으로 필요한 데이터만 비교하기 - 729
from sortedcontainers import SortedSet

class MyCalendar:

    def __init__(self):
        # MyCalendar 객체에 필요한 속성 정의
        self.events = SortedSet()

    def book(self, start: int, end: int) -> bool:
        idx = self.events.bisect_left((start, end))

        if idx > 0: # idx가 0인 경우에는 이전 이벤트가 존재하지 않으므로 패스
            prev_event = self.events[idx - 1]
            if prev_event[1] > start: # 이전 이벤트의 종료시각보다 새 이벤트가 먼저 시작하면
                return False
        if idx < len(self.events): # idx가 len(self.events)인 경우는 이후 이벤트가 존재하지 않으므로 패스
            next_event = self.events[idx]
            if next_event[0] < end: # 다음 이벤트의 시작시각보다 새 이벤트가 늦게 끝나면
                return False

        self.events.add((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)