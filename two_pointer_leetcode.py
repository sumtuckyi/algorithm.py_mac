class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # words1 = deque(sentence1.split())
        # words2 = deque(sentence2.split())

        # # 접두사 비교
        # while words1 and words2 and words1[0] == words2[0]:
        #     words1.popleft()
        #     words2.popleft()
        # # 접미사 비교
        # while words1 and words2 and words1[-1] == words2[-1]:
        #     words1.pop()
        #     words2.pop()

        # # 둘 중 하나라도 비어있는지 반환
        # return not words1 or not words2

        words1 = sentence1.split()
        words2 = sentence2.split()

        start, e1, e2 = 0, len(words1) - 1, len(words2) - 1

        if len(words1) > len(words2):  # words1의 길이가 더 짧게 일관성을 유지한다.
            return self.areSentencesSimilar(sentence2, sentence1)

        # 앞에서부터 순서대로 단어가 일치하는지 비교하되, 더 짧은 문장이 끝날 때까지 진행한다.
        while start < len(words1) and words1[start] == words2[start]:
            start += 1

        while e1 >= 0 and words1[e1] == words2[e2]:
            e1 -= 1
            e2 -= 1

        # 여기서 e1은 더 짧은 문장의 탐색 종료 인덱스
        # e1 < start 라는 것은 문장1의 모든 단어가 다른 문장과 일치하여 제거될 수 있음을 의미한다.
        return e1 < start
