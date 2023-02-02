#Chapter10 Excercise

#10.1 아무 내용이 없는 Thing 클래스를 만들어서 출력한다. 이 클래스의 example 객체를 생성해서 출력한다. 이 때 두 출력값은 같은가?

class Thing():
    pass
example=Thing()

print(Thing())
print(example)
"다르다"

#10.2 Thing2 클래스를 만들고, 이 클래스의 letters 속성에 값 'abc'를 할당한 후 letters를 출력해보자
class Thing2():
    letters = 'abc'

print(Thing2().letters)

# 10.3 Thing3 클래스를 만든다. 이번에는 인스턴스의 letters 속성에 값 'xyz'를 할당한 후
# letters를 출력한다. letters를 출력하기 위해 객체를 생성해야 하는가?

class Thing3():
    letters = 'xyz'

print(Thing3().letters)
"아뇨"

# 10.4 name, symbol, number 인스턴스 속성을 가진 Element 클래스를 만들어보자.
#      이 클래스에서 'Hydrogen, 'H', 1 값을 가진 객체를 생성한다.

class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol = symbol
        self.number = number

Suso=Element("Hydrogen","H",1)
print(Suso.name,Suso.symbol,Suso.number)


# 10.5 "name": "Hydrogen", "symbol":"H","number":1과 같이 키와 값으로 이루어진
#      el_dict 딕셔너리를 만들어보자. 그리고 el_dict 딕셔너리로부터 Element 클래스의 hydrogen 개게를 생성한다.

class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol = symbol
        self.number = number

el_dict={"name": "Hydrogen", "symbol":"H","number": 1}
hydrogen=Element(el_dict.get("name"),el_dict.get("symbol"),el_dict.get("number"))
print(hydrogen.name,hydrogen.symbol,hydrogen.number)

# 10.6 Element 클래스에서 객체의 속성(name, symbol, number) 값을 출력하는 dump() 메서드를 정의한다.
#      이 클래스의 hydrogen 객체를 생성하고, dump() 메서드로 이 속성을 출력한다.

class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

hydrogen = Element("Hydrogen","H",1)
hydrogen.dump()

# 10.7 print(hydrogen)을 호출한다. Element 클래스의 정의에서 dump 메서드를 __str__() 메서드로 바꿔서 새로운 hydrogen 객체를 생성한다.
#      그리고 print(hydrogen)을 다시 호출한다.

print(hydrogen)

class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f"{self.name} {self.symbol} {self.number}"

hydrogen = Element("Hydrogen", "H", 1)
print(hydrogen)


#10.8  Element 클래스를 수정해서 name, symbol, number의 속성을 private으로 만든다.
#      각 속성값을 반환하기 위해 getter 프로퍼티를 정의한다.

class Element:
    def __init__(self,name,symbol,number):
        self.hidden_name=name
        self.hidden_symbol = symbol
        self.hidden_number = number

    @property
    def get_name(self):
        return self.hidden_name

    @property
    def get_symbol(self):
        return self.hidden_symbol

    @property
    def get_number(self):
        return self.hidden_number

    def __str__(self):
        return f"{self.get_name} {self.get_symbol} {self.get_number}"

hydrogen = Element("Hydrogen", "H", 1)
print(hydrogen)


