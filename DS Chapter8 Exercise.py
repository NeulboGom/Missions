# Chapter8 Exercise01 편의점에서 판매된 물건 목록 출력하기

import random

real_list = ['레쓰비캔커피', '도시락', '삼각김밥', '코카콜라', '삼다수', '츄파춥스']
real_list = [random.choice(real_list) for _ in range(20)]


class TreeNode():
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


root = None
node = TreeNode(real_list[0])
root = node

for i in real_list[1:]:
    node = TreeNode(i)

    current = root
    while True:
        if node.data == current.data:
            break
        if node.data < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right


def preorder(element):
    if element is None:
        return
    print(element.data, end=' ')
    preorder(element.left)
    preorder(element.right)


print(f"오늘 판매된 물건(중복 O) --> {real_list}")
print("Binary Search Tree 구성 완료!")
print(f"오늘 판매된 종류(중복 X) -->", end=' ')
preorder(root)
