# deque 활용하기 - 1813
from collections import deque
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = deque(sentence1.split())
        words2 = deque(sentence2.split())

        # 접두사 비교
        while words1 and words2 and words1[0] == words2[0]:
            words1.popleft()
            words2.popleft()
        # 접미사 비교
        while words1 and words2 and words1[-1] == words2[-1]:
            words1.pop()
            words2.pop()

            # 둘 중 하나라도 비어있는지 반환
        return not words1 or not words2