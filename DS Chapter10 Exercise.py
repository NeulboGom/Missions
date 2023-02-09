# Chapter10 Exercise 진수 변환하기

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_list += ['A', 'B', 'C', 'D', 'E', 'F']


def arith_from_d(x, ari):
    if x < ari:
        print(num_list[x], end='')
    else:
        arith_from_d(x // ari, ari)
        print(num_list[x % ari], end='')


de_x = int(input("10진수 입력 : "))
print(f"2진수 : {arith_from_d(de_x, 2)}\n")
print(f"8진수 : {arith_from_d(de_x, 8)}\n")
print(f"16진수 : {arith_from_d(de_x, 16)}\n")