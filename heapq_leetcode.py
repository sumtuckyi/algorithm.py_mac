class KthLargest(object):


    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        #최소힙에 아직 k보다 적은 수의 요소가 있거나 힙의 최솟값보다 추가되는 값이 큰 경우에만 힙에 val을 추가
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            # k보다 힙의 길이가 길어지면, 가장 작은 수를 삭제 -> 길이를 k로 유지
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        #힙의 길이는 항상 k보다 작거나 같기 때문에 0번째 요소가 k번째로 큰 요소가 된다.
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)