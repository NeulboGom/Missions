# Exercise 02 콜센터의 응답 대기 시간 계산하기

SIZE = 6
front, rear = 0, 0
queue = [None for _ in range(SIZE)]


def isqueue_full():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
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
        return
    return queue[front + 1]


def en_queue(data):
    global SIZE, queue, front, rear
    if isqueue_full():
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def de_queue(data):
    global SIZE, queue, front, rear
    if isqueue_empty():
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


call_list = [("사용", 9), ("고장", 3), ("환불", 4), ("환불", 4), ("고장", 3)]

time = 0

for i in call_list:
    print(f"귀하의 대기 예상 시간은 {time}분 입니다.")
    print(f"현재 대기 콜 --> {queue}")
    print()
    en_queue(i)
    time += i[1]


print(f"최종 대기 콜 --> {queue}")
print("프로그램 종료!")
