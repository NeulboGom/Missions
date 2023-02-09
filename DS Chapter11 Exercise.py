# Chapter11 Exercise02 2차원 배열의 중앙값 찾기

matrix = [[55, 33, 250, 44],
          [88, 1, 76, 23],
          [199, 222, 38, 47],
          [155, 145, 20, 99]]


def mtx_to_list(mtx):
    mtx_list = []
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            mtx_list.append(matrix[i][j])
    return mtx_list


new_list = mtx_to_list(matrix)
print(f"1차원 변경 후, 정렬 전 --> {new_list}")


def insertion_sort(ls):
    n = len(ls)
    for end in range(n):
        for cur in range(end,0, -1):
            if ls[cur - 1] > ls[cur]:
                ls[cur - 1], ls[cur] = ls[cur], ls[cur - 1]
    return ls


new_sort_list = insertion_sort(new_list)


print(f"1차원 변경 후, 정렬 후 --> {new_sort_list}")
print(f"중앙값 --> {new_sort_list[len(new_sort_list) // 2]}")