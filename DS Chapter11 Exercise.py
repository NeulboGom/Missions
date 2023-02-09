# Chapter11 Exercise01 성적 별로 조 편성하기

## 전역 함수 선언 부분 ##
stud_list = [["선미", 88], ["초아", 99], ["화사", 71], ["영탁", 78], ["영웅", 67], ["민호", 92]]


## 함수 선언 부분 ##
def quick_sort(ls):
    n = len(ls)
    if n <= 1:
        return ls

    pivot = ls[n//2]
    left_ls, right_ls, middle_ls = [], [], []

    for i in range(n):
        if ls[i][1] < pivot[1]:
            left_ls.append(ls[i])
        elif ls[i][1] > pivot[1]:
            right_ls.append(ls[i])
        else:
            middle_ls.append(ls[i])
    return quick_sort(left_ls) + middle_ls + quick_sort(right_ls)


print(f"정렬 전 --> {stud_list}")
sort_stud_list = quick_sort(stud_list)
print(f"정렬 후 --> {sort_stud_list}")
print("##성적별 조 편성표##")
for i in range(len(stud_list) // 2):
    print(f"{sort_stud_list[i][0]} : {sort_stud_list[-1-i][0]}")
