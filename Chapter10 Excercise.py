#Chapter10 Excercise

# 10.9 세 클래스 Bear, Rabbit, Octothorpe를 정의한다. 각 클래스에 eats() 메서드를 정의해보자
#      각 메서드는 'berries'(Bear), 'clover'(Rabbit), 'campers'(Octothorpe) 를 반환한다.
#      각 클래스의 객체를 생성하고 eats() 메서드의 반환값을 출력한다.

class Bear():
    def __init__(self, name, food):
        self.name = name
        self.food = food
    
    def eats(self):
        return f"'{self.food}' ({self.name})"

class Rabbit():
    def __init__(self, name, food):
        self.name = name
        self.food = food
    
    def eats(self):
        return f"'{self.food}' ({self.name})"

class Octothorpe():
    def __init__(self, name, food):
        self.name = name
        self.food = food
    
    def eats(self):
        return f"'{self.food}' ({self.name})"

Gom = Bear("Bear","berries")
Tokki = Rabbit("Rabbit","clover")
Sharp = Octothorpe("Octothorpe","campers")

print(Gom.eats())
print(Tokki.eats())
print(Sharp.eats())

#10.10 Laser, Claw, SmartPhone 클래스를 정의한다. 각 클래스는 does() 메서드를 갖고 있다.
#      각 메서드는 'distintegrate'(Laser), 'crush'(Claw) 또는 'ring'(Smart Phone) 을 반환한다.
#      그리고 각 인스턴스(객체)를 갖는 Robot 클래스를 정의한다.
#      Robot 클래스의 객체가 갖고 있는 내용을 출력하는 does() 메서드를 정의한다.

class Laser():
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def does(self):
        return f"'{self.action}' ({self.name})"

class Claw():
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def does(self):
        return f"'{self.action}' ({self.name})"

class SmartPhone():
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def does(self):
        return f"'{self.action}' ({self.name})"

laser = Laser("Laser","distintegrate")
claw = Claw("Claw", "crush")
smartphone = SmartPhone("Smart Phone", "ring")

print(laser.does())
print(claw.does())
print(smartphone.does())
