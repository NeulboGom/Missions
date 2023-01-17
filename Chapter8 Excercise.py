#Chapter8 Excercise

#8.1 영어-프랑스어 사전을 의미하는 e2f 딕셔너리를 만들어 출력해보자. 영어 dog는 프랑스어 chien이고, cat은 chat, walrus는 morse다.
e2f={"dog":"chien","cat":"chat","walrus":"morse"}

#8.2 e2f 딕셔너리에서 영어 walrus를 프랑스어로 출력해보자
print(e2f["walrus"])

#8.3 e2f 딕셔너리에서 f2e 딕셔너리라는 영어-프랑스어 사전을 만들어보자(items method 사용)
f2e={}
for key,value in e2f.items():
    f2e[value]=key
print(f2e)

#8.4 ef2딕셔너리를 사용해서 프랑스어 chien을 영어로 출력해보자
print(f2e["chien"])

#8.5 e2f 딕셔너리의 영어 단어 키들을 출력해보자
print(e2f.keys())

#8.6 이차원 딕셔너리 life를 만들어보자. 최상위 키는 'animals','plants','other'다.
#    그리고 'animals'는 각각 'cats', 'octopi','emus'를 키로 하고,
#    'Henri','Grumpy','Lucy'를 값으로 하는 또 다른 딕셔너리를 참조하고 있다
#    나머지 요소는 빈 딕셔너리를 참조한다

life={"animals": {"cats":"Henri","octopi":"Grumpy","emus":"Lucy"},
      "plants":{},
      "others":{}}

#8.7 life 딕셔너리의 최상위 키를 출력해보자
print(life.keys())

#8.8 life['animals']의 모든 키를 출력해보자
print(life['animals'].keys())

#8.9 life['animals]['cats']의 모든 값을 출력해보자
print(life['animals'].get('cats'))

#8.10 딕셔너리 컴프리헨션으로 squares 딕셔너리를 생성한다. range(10)를 키로 하고 각 키의 제곱을 값으로 한다.
squares={num:num**2 for num in range(10)}
print(squares)