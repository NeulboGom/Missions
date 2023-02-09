# Chapter11 Exercise01 성적 별로 조 편성하기

## 전역 함수 선언 부분 ##
stud_list = [["선미", 88], ["초아", 99], ["화사", 71], ["영탁", 78], ["영웅", 67], ["민호", 92]]


## 함수 선언 부분 ##

def insertion_sort(ls):
    n = len(ls)
    for i in range(1, n):
        for cur in range(i, 0, -1):
            if ls[cur-1][1] > ls[cur][1]:
                ls[cur-1], ls[cur] = ls[cur], ls[cur-1]
    return ls


print(f"정렬 전 --> {stud_list}")
sort_stud_list = insertion_sort(stud_list)
print(f"정렬 후 --> {sort_stud_list}")
print("##성적별 조 편성표##")
for i in range(len(stud_list) // 2):
    print(f"{sort_stud_list[i][0]} : {sort_stud_list[-1-i][0]}")
