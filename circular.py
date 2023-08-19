# def enq(data):
#     global rear, front
#     if (rear+1) % qsize == front:
#         front = (front+1) % qsize
#         q[(rear+1) % qsize] = data
#     else:
#         rear = (rear+1) % qsize
#         q[rear] = data
#
# def sliding(deg):
#     global front, rear
#     n = deg//90
#     front += 1
#     rear = (rear+1) % qsize
#     temp = q[front % qsize]
#     q[front % qsize] = q[(front - 1) % qsize]
#     for i in range(1, 4*n-1):
#         front += 1
#         q[(front) % qsize], temp = temp, q[(front) % qsize]
#
#
# qsize = 4
# q = [0]*qsize
# front = -1
# rear = -1
# end = -1
#
# enq(12)
# enq(3)
# enq(6)
# enq(9)
# print(q)
# print(front, rear)
# sliding(180)
# print(q)

def sliding(deg):
    n = deg//90
    temp = q[1]
    q[1] = q[0]
    for i in range(2*n):
        q[(i+1)%qsize], temp = temp, q[(i+1)%qsize]




q = [3, 6, 9, 12]
qsize = 4
sliding(180)
print(q)
# sliding(450)
# print(q)