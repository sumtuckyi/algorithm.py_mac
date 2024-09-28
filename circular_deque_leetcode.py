# 양방향 삽입, 삭제가 가능한 원형 큐 구현하기 - 641
class MyCircularDeque:

    def __init__(self, k: int): # 최대크기 k의 deque 생성
        self.queue = [0] * k # fixed array 사용
        self.front = 0
        self.rear = k - 1
        self.size = 0 # 현재 몇 개의 원소가 존재하는지 관리
        self.capacity = k


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # 포인터만 이동하고 값을 삭제하지는 않음 - 어차피 삽입 시에 덮어쓸 것이기 때문
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()