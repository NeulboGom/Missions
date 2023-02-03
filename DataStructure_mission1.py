# P115 응용예제 modified


'''

폐기:
기존 hp 1000보다 높은 값 ["잠만보", 5000]을 가지는 값을 넣고
다시 1000과 동일한 값을 ["한카리아스", 1000] 넣으려고 했을 때,
처음부터 반복돼서 1000<5000으로 인식돼서 elif2번이 돌아서 append 됨
책의 자료 참고해서 다시 만들 예정

pokemons = [['망나뇽', 1000], ['루기아', 1000], ['리자몽', 800], ['피카츄', 500], ['잉어킹', 150]]


def add_poke(nm, hp):
    list_val = [nm, hp]
    for i in range(len(pokemons)):
        if int(hp) == int(pokemons[0][1]):
            print("if")
            pokemons.insert(0, list_val)
            break
        elif int(hp) >= int(pokemons[i][1]):
            print("elif1")
            pokemons.insert(i, list_val)
            break
        elif int(hp) < int(pokemons[i][1]):
            print("elif2")
            pokemons.append(list_val)
            break
        # elif int(hp) != int(pokemons[0][1]):
        #     print("elif3")
        #     break
    return pokemons


while True:
    selection = input("1. 포켓몬 추가 / 2. 종료:  ")
    if selection == '1':
        name = input("추가할 포켓몬: ")
        count = input("포켓몬의 체력: ")
        add_poke(name, count)
        print(pokemons)
    elif selection == '2':
        print("종료합니다.")
        break
    else:
        print("메뉴를 골라주세요")

'''