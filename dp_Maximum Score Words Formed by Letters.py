from collections import Counter

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        self.letter_count = Counter(letters)  # letters를 해시 테이블로 변환
        self.score = score  # 점수 배열
        self.memo = {} # dp 딕셔너리

        # 모든 단어의 점수 미리 계산
        word_scores = []
        for word in words:
            word_score = 0
            for char in word:
                word_score += score[ord(char) - ord('a')]
            word_scores.append(word_score)
        print(word_scores)
        # DP를 이용하여 최대 점수 계산
        return self.dfs(words, word_scores, 0, self.letter_count)

    def dfs(self, words, word_scores, index, letter_count):
        '''
        index번째 단어를 선택할 차례이며 현재 남은 문자의 개수를 letter_count가 담고 있음
        이 경우의 최대 점수가 이미 계산된 적이 있으면 해당 값을 사용
        계산된 적이 없으면 단어를 선택하지 않고 다음 단어로 넘어가는 경우와
        단어를 선택하는 경우로 분기함
        단어를 선택하는 경우에는 현재 남은 문자로 이 단어를 만들 수 있는지 확인하고
        만들 수 없다면 이 단어를 만들지 않은 상태로 다음 단어를 탐색
        만들 수 있다면 이 단어를 만든 상태로 다음 단어를 탐색

        '''
        if index == len(words):
            return 0

        key = (index, tuple(letter_count.items()))  # 메모이제이션 딕셔너리에서 사용하는 키
        if key in self.memo:
            return self.memo[key]

        # 단어를 선택하지 않는 경우
        max_score = self.dfs(words, word_scores, index + 1, letter_count.copy())

        # 단어를 선택할 수 있는 경우
        can_take = True
        new_letter_count = letter_count.copy()
        for char in words[index]:  # index번째 단어를 만들 수 있는 있는지 확인
            if new_letter_count.get(char, 0) <= 0:
                can_take = False
                break
            new_letter_count[char] -= 1

        if can_take: # index번째 단어를 만들 수 있으니, 이 단어를 만들고 남은 문자 배열을 인자로 하여 다음 단어를 탐색
            # 여기서 최종으로 return할 점수의 최댓값이 업데이트 됨
            max_score = max(max_score, word_scores[index] + self.dfs(words, word_scores, index + 1, new_letter_count))

        self.memo[key] = max_score
        return max_score


# Example usage
solution = Solution()  # Solution 클래스의 인스턴스 생성
words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
print(solution.maxScoreWords(words, letters, score))  # 예시 출력
print(solution.memo)