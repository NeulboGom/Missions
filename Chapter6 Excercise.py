#Chatper6 Excercise

#6.1
for i in range(3,-1,-1):
    break
print(list(range(3,-1,-1)))

#6.2

guess_me=7
number=1
while True:
    if number==guess_me:
        print("found it!")
        break
    elif number>guess_me:
        print("oops")
        break
    elif number<guess_me:
        print("too low")
    number+=1

#6.2
guess_me2=5
for number2 in range(10):
    if number2==guess_me2:
        print("found it!")
        break
    elif number2>guess_me2:
        print("oops")
        break
    elif number2<guess_me2:
        print("too low")