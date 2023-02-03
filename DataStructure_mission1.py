# P115 응용예제 modified


pokemons = [['망나뇽', 1000], ['루기아', 1000], ['리자몽', 800], ['피카츄', 500], ['잉어킹', 150]]


def location_poke(nm,hp):
    list_poke = [nm,hp]
    idx = -1        # for문에서 돌다가, 마지막일 순번까지 조건에 안 맞는 경우를 가정한듯
    for i in range(len(pokemons)):
        if int(hp) >= int(pokemons[i][1]):
            idx = i     # 들어갈 위치 찾기
            break
    if idx == -1:
        idx = len(pokemons)     # 마지막 순번(pokemons[4][1])보다 작을 때, pokemons[5]에 들어가도록 하는 것

    add_poke(idx,list_poke)       #함수 안에 함수를 넣어서 location 함수만으로 넣을 수 있게...?


def add_poke(add_pos,lists):
    if add_pos<0 or add_pos>len(pokemons):      # 범위 밖의 idx가 입력될 경우... 거진 없을 듯
        print("데이터 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)           # 일단 None으로 뒤에 빈 공간 만들어서 앞에가 뒤로 밀릴 수있게 하는 빅픽쳐
    len_of_poke=len(pokemons)

    for i in range(len_of_poke-1, add_pos, -1):   # 큰 그림의 끝: 길이(index)부터 -1씩 위에서 나온 idx까지 떨어지는 i
        pokemons[i] = pokemons[i-1]             # 앞에께 한칸씩 뒤로 밀림 ex)2번자리가 3번자리로
        pokemons[i-1] = None                    # 그리고 빈 자리(add_pos 혹은 idx)를 None으로 채움 ex) 2번자리가 None으로

    pokemons[add_pos] = lists                    # 화룡정점: idx위치에 16번 줄에 준비해둔 리스트 넣음


while True:
    selection = input("1. 포켓몬 추가 / 2. 종료:  ")
    if selection == '1':
        name = input("추가할 포켓몬: ")
        count = input("포켓몬의 체력: ")
        location_poke(name, count)
        print(pokemons)
    elif selection == '2':
        print("종료합니다.")
        break
    else:
        print("메뉴를 골라주세요")

