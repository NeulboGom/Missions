#Chpter5 Excercise

#5.4
letter='''Dear {} {},
        Thank you for your letter. We are sorry that our {} {} in your
    {}. Please note that it should never be used in a {}, especially near any
    {}.
        
        Send us your receipt and {} for shipping and handling. We will send you
    another {} that, in our tests, is {}% less likely to have {}.
    
        Thank you for your support.
        Sincerely,
        {}
        {}'''
salutation="nice"
name="Kim"
product="Assult Riple"
verbed="used"
room="bedroom"
animals="dogs"
amount="the amount"
percent="5"
spokeman="Mr.Rho"
job_title="Samsung"

print(letter.format(salutation, name, product, verbed, room, room, animals, amount, product, percent, verbed, spokeman, job_title))


#5.6

first="duck"
second="gourd"
third="spitz"
cap_first=first.capitalize()
cap_second=second.capitalize()
cap_third=third.capitalize()

print('''%sy Mc%sface
%sy Mc%sface
%sy Mc%sface''' % (cap_first, cap_first, cap_second, cap_second, cap_third, cap_third))

#5.7
print('''{}y Mc{}face
{}y Mc{}face
{}y Mc{}face'''.format(cap_first, cap_first, cap_second, cap_second, cap_third, cap_third))

print(f'''{cap_first}y Mc{cap_first}face
{cap_second}y Mc{cap_second}face
{cap_third}y Mc{cap_third}face''')

