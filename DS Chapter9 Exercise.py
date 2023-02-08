# Chapter9 Exercise01 허니버터 칩이 가장 많이 남은 편의점 찾기


# size * size 크기의 0행렬 만듦
class Graph():
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print(' ', end=' ')
    for i in range(len(store_list)):
        print(store_list[i][0], end=' ')
    print()
    for row in range(g.size):
        print(store_list[row][0], end=' ')
        for col in range(g.size):
            print(g.graph[row][col], end=' ')
        print()


## 전역변수 선언 부분 ##
G1 = None
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4
store_list = [["GS25", 30], ["CU", 60], ["Seven11", 10], ["MiniStop", 90], ["Emart24", 40]]

## 메인 코드 부분 ##
graph_size = 5
G1 = Graph(graph_size)
G1.graph[GS25][CU] = G1.graph[GS25][Seven11] = 1
G1.graph[CU][GS25] = G1.graph[CU][Seven11] = G1.graph[CU][3] = 1
G1.graph[Seven11][GS25] = G1.graph[Seven11][CU] = G1.graph[Seven11][MiniStop] = 1
G1.graph[MiniStop][CU] = G1.graph[MiniStop][Seven11] = G1.graph[MiniStop][Emart24] = 1
G1.graph[Emart24][MiniStop] = 1

print("## 편의점 그래프 ##")
print_graph(G1)
print()

stack = []
visit_store = []

current = 0
store_max = current
store_max_num = store_list[current][1]
stack.append(current)
visit_store.append(current)


while len(stack) != 0:
    ne_xt = None
    for vertex in range(graph_size):
        if G1.graph[current][vertex] == 1:
            if vertex in visit_store:
                pass
            else:
                ne_xt = vertex
                break

    if ne_xt is not None:
        current = ne_xt
        stack.append(current)
        visit_store.append(current)
        if store_list[current][1] > store_max_num:
            store_max_num = store_list[current][1]
            store_max = current
    else:
        current = stack.pop()


print(f"허니버터칩 최대 보유 편의점(개수) --> {store_list[store_max][0]}({store_max_num})")
