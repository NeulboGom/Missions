#Chapter9 Excercise

#9.1 ['Harry','Ron', 'Hermione'] 리스트를 반환하는 good()함수를 정의해보자

def good():
    return ['Harry', 'Ron', "Hermione"]
print(good())

#9.2 range(10)의 홀수를 반환하는 get_odds 제너레이터 함수를 정의해보자
#    for문으로 반환된 세 번째 홀수를 찾아서 출력한다.

def get_odd():
    for number in range(10):
        if number%2!=0:
            yield number

print(get_odd())
list_odd_number=[answer for answer in get_odd()]
print(list_odd_number[2])

count=0             #다른 방법
for i in get_odd():
    count += 1
    if count == 3:
        print(i)

#9.3 어떤 함수가 호출되면 'start'를, 끝나면 'end'를 출력하는 test 데커레이터를 정의해보자.
def test_decorator(func):
    def wrapper():
        print(func.__name__,"start")
        func()
        print(func.__name__,"end")
        return func
    return wrapper()

@test_decorator
def printing():
    print("It works")


printing()


#  OopsException 예외를 정의해보자. 이 예외를 발생시켜보자.
#  그리고 이 예외를 잡아서 'Caught an oops'를 출력하는 코드를 작성해보자

class OopsException(Exception):
    pass

try:
    raise OopsException("Caught an oops")
except Exception as exc:
    print(exc)