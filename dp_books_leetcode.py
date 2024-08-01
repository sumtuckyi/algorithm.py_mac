# dp - top-down방식 접근법
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        self.n = [len(books)]
        # memoization - memo[i][j]는 i번째까지 책을 꽂았고, 남은 폭이 j일 때, 최소  총 높이
        memo = [[0 for _ in range(1001)] for _ in range(self.n[0])]
        return self._dpHelper(books, shelfWidth, memo, 0, shelfWidth, 0)

    def _dpHelper(self, books, shelf_w, memo, i, remaining_w, max_h):  # max_h은 현재 보고 있는 선반에서 가장 높은 책의 높이
        cur_book = books[i]  # i번째 책을 어디 놓을지 결정할 것임
        new_max_h = max(max_h, cur_book[1])  # 현재 선반의 최고 높이랑 새로 꽂을 책의 높이를 비교

        # 마지막 책인 경우 - 재귀호출 종료 조건
        if i == self.n[0] - 1:
            # 현재 선반에 둘 곳이 있다면
            if remaining_w >= cur_book[0]:
                return new_max_h
            # 현재 선반에 놓을 수 없다면 다음 선반에 놓는다.
            return max_h + cur_book[1]

            # memoization
        if memo[i][remaining_w] != 0:  # 현재 상황이 이미 계산된적 있으면
            return memo[i][remaining_w]
        else:  # 그렇지 않다면 계산
            # 새 선반에 놓는 경우
            new_line_h = max_h + self._dpHelper(
                books, shelf_w, memo, i + 1, shelf_w - cur_book[0], cur_book[1]
            )
            # 기존 선반에 만약 남은 공간이 충분하다면
            if remaining_w >= cur_book[0]:
                stay_line_h = self._dpHelper(
                    books, shelf_w, memo, i + 1, remaining_w - cur_book[0], new_max_h
                )
                memo[i][remaining_w] = min(new_line_h, stay_line_h)
                return memo[i][remaining_w]

            # 기존 선반에 놓을 수 없는 경우 memo 배열 업데이트
            memo[i][remaining_w] = new_line_h
            return memo[i][remaining_w]

# bottom-up 방식 - 선호
class Solution2(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [0] * (n + 1)

        # dp배열 초기화
        dp[0] = 0
        dp[1] = books[0][1]

        for i in range(2, n + 1):
            # i-1번째까지의 책을 모두 꽂았을 때의 최소 높이
            remaining_w = shelfWidth - books[i - 1][0]
            max_h = books[i - 1][1]
            dp[i] = books[i - 1][1] + dp[i - 1]

            j = i - 1  # 현재 꽂을 책의 인덱스
            while j > 0 and remaining_w - books[j - 1][0] >= 0:
                max_h = max(max_h, books[j - 1][1])
                remaining_w -= books[j - 1][0]
                dp[i] = min(dp[i], max_h + dp[j - 1])
                j -= 1
        print(dp)
        return dp[n]


