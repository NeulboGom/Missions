#Chapter7 Excercise

#7.10 리스트 컴프리헨션을 이용하여 range(10)에서 짝수 리스트를 만들어보자
even_number=[i for i in range(10) if i%2==0]
print(even_number)

#7.11 줄넘기 랩 음악을 만들어보자. 일련의 두 줄 리듬을 출력한다. 프로그램의 시작부분은 다음과 같다
start1=["fee","fie","foe"]
rhymes=[
    ("flop","get a mop"),
    ("fope","turn the rope"),
    ("fa","get your ma"),
    ("fudge", "call the judge"),
    ("fat","pet the cat"),
    ("fog","walk the dog"),
    ("fun","say we're done"),
]
start2="Someone better"

#rhymes의 각 튜플(첫 번째, 두 번째)에서
#첫 번째: 1. start1의 각 문자열을 출력한다. 첫 글자를 대문자로 만들고, 각 단어 뒤에 느낌표와 공백을 출력한다.
#첫 번째: 2. 이어서 rhymes의 첫 번째 문자열의 단어 역시 첫 글자를 대문자로 만들고 대문자를 출력한다.

#두 번째: 1. start2와 공백을 출력한다.
#두 번째: 2. 두 번째 문자열과 마침표를 출력한다.
'''
start1=[start1[i].capitalize() for i in range(len(start1))]
delimiter="! "
exclamed_start1=delimiter.join(start1)+'! '
print(start1)
print(exclamed_start1)
'''
for (j,k) in rhymes:
    # start1=["fee","fie","foe"]
    for i in start1:
        print(i.capitalize(), end='! ')
    print(j.capitalize(), end='! \n')
    print(start2, end=' ')
    print(k, end='. \n')