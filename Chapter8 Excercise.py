#Chapter8 Excercise

#8.11 셋 컴프리헨션을 이용하여 range(10)에서 홀수 셋을 만든다.
odd_set={number for number in range(10) if number%2!=0}
print(odd_set)

#8.12 제너레이터 컴프리헨션을 이용하여 문자열 'Got'과 range10의 각 숫자를 반환한다.
#     for 문을 사용해서 제너레이터를 순회한다.
gen_=(n for n in range(10))
for v in gen_:
    print("Got",v)

#8.13 zip()을 사용해서 딕셔너리를 생성한다. key로 ('optimist','pessimist','troll') 튜플을 사용하고
#     값으로 ('The glass is half full','The glass is half emplty','How did you get a glass?') 튜플을 사용한다
tuple_keys=('optimist', 'pessimist', 'troll')
tuple_values=('The glass is half full',
              'The glass is half empty',
              'How did you get a glass?')
answer_dict={}
for key,value in zip(tuple_keys, tuple_values):
    answer_dict[key]=value
print(answer_dict)

#8.14  zip()을 사용해서 다음 두 리스트를 짝으로 하는 movies 딕셔너리를 만들어보자
titles=['Creature of Habit', 'Crewel Fate']
plots=['A nun turns into a mon ster', 'A haunted yarn shop']
required_dict={}
for t,p in zip(titles,plots):
    required_dict[t]=p
print(required_dict)