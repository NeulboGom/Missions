# Exercise 01 유명 맛집의 대기줄 구현하기

front, rear = -1, 4
SIZE = 5
queue = ['정국', '뷔', '지민', '지민', '슈가']


def isqueue_full():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        return True
    else:
        return False

def isqueue_empty():
    global SIZE, queue, front, rear
    if rear == front:
        return True
    else:
        return False


def peek():
    global SIZE, queue, front, rear
    if isqueue_empty():
        print("No data in queue")
        return
    else:
        return queue[front+1]


def en_queue(data):
    global SIZE, queue, front, rear
    if isqueue_full():
        print("queue is full!")
        return
    rear += 1
    queue[rear] = data


def de_queue(data):
    global SIZE, queue, front, rear
    if isqueue_empty():
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front + 1, SIZE):
        queue[i - 1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1

    return data


while True:
    print(f"대기 줄 상태: {queue}")
    print(f"{queue[0]} 님 식당에 들어감")
    de_queue(queue[0])
    if isqueue_empty():
        print(f"대기 줄 상태: {queue}")
        print("식당 영업 종료!")
        break
