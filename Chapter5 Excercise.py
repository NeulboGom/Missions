#Chpter5 Excercise

#5.1 m으로 시작하는 단어를 대문자로 만들어보자.
song="""When an eel grabs your arm,
And it causes great harm,
Tha's - a moray!"""

simple_song=song.strip("!")
list_song=simple_song.split()

for word in list_song:
    if word.startswith("m"):
        capital_word=word.capitalize()
        print(capital_word)
list_song[-1]=capital_word
print(list_song)

for i in list_song:
    remake_song=" ".join(list_song)
print(remake_song)


#5.2
question=["We don't serve strings around here. Are you a string?",
          "What is said on Father's Day in the forest?",
          "What makes the sound 'Sis! Boom! Bah!'?"]
answers=["An exploding sheep.",
         "No, I'm a frayed knot.",
         "'Pop!' goes the weasel."]
for i in range(0,3):
    print(f"Q:{question[i]}\nA:{answers[i]}\n")

#5.3
print('''My kitty cat likes %s
My kitty cat likes %s
My kitty cat fell on his %s And now thinks he's a %s''' %("roast beef", "ham","head","clam"))

#5.4
letter='''Dear {salutation} {name},
        Thank you for your letter. We are sorry that our {product} {verbed} in your
    {room}. Please note that it should never be used in a {room}, especially near any
    {animals}.
        
        Send us your receipt and {amount} for shipping and handling. We will send you
    another {product} that, in our tests, is {percent}% less likely to have {verbed}.
    
        Thank you for your support.
        Sincerely,
        {spokeman}
        {job_title}'''
salutation="nice"
name="Kim"
product="Assult Riple"
verbed="used"
room="bedroom"
amount="the amount"
percent="5"
spokeman="Mr.Rho"
job_title="Samsung"

print(letter.format(salutation, name, product, verbed, room, amount, percent, spokeman, job_title))