# Chapter13 Exercise01 편의점에서 판매되는 물건 목록과 개수 세기

import random

sold_list = ['코카콜라', '츄파춥스', '도시락', '삼각김밥', '레쓰비캔커피', '바나나맛 우유']
today_list_notsorted = [random.choice(sold_list) for _ in range(20)]
print(f"# 오늘 판매된 전체 물건(중복O, 정렬X) --> {today_list_notsorted}")

today_list_sorted = sorted(today_list_notsorted)
print(f"# 오늘 판매된 전체 물건(중복O, 정렬O) --> {today_list_sorted}")

today_list = list(set(today_list_notsorted))
print(f"# 오늘 판매된 물품 종류(중복X) --> {today_list}")


def binary_search(ls, searching_data):
    idx = -1
    start = 0
    end = len(ls) - 1
    while start <= end:
        mid = (start + end) // 2
        if ls[mid] == searching_data:
            idx = mid
        elif ls[mid] < searching_data:
            start = mid + 1
        elif ls[mid] > searching_data:
            end = mid - 1

    return idx



final_sell_list = []
count = 0
for stuff in today_list:
   count = today_list_sorted.count(stuff)
   final_sell_list.append((stuff, count))

print(f"결산 결과 --> {final_sell_list}")
