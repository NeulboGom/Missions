# Chapter13 Exercise02 순차 검색과 이진 검색의 성능 비교하기

import random

num_list_not_sorted = [random.randint(0, 999999) for _ in range(1000000)]
num_list_sorted = sorted(num_list_not_sorted)


# 순차 검색
count_sequence = 0


def sequence_search(ls, data):
    global count_sequence
    idx = -1
    size = len(ls)
    for i in range(size):
        count_sequence += 1
        if ls[i] == data:
            idx = i
            break
    return idx


# 이진 검색
count_binary = 0


def binary_search(ls, data):
    global count_binary
    start = 0
    end = len(ls) - 1
    while start <= end:
        count_binary += 1
        mid = (start + end) // 2
        if ls[mid] == data:
            return mid
        elif ls[mid] < data:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print(f"# 비정렬 배열(100만개) -> {num_list_not_sorted}")
print(f"# 정렬 배열(100만개) -> {num_list_sorted}")

f_data = random.choice(num_list_not_sorted)
sequence_search(num_list_not_sorted, f_data)
print(f"순차 검색(비정렬 데이터) --> {count_sequence}회")
binary_search(num_list_sorted, f_data)
print(f"이진 검색(정렬 데이터) --> {count_binary}회")
