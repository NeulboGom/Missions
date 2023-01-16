#Chapter7 Excercise

#7.1 출생 년도에 대한 리스트 years_lists를 만들어보자 ex) 1980,1981,1982~~
years_lists=[1980,1981,1982,1983,1984,1985]

#7.2 years_lists의 세 번째 생일은 몇 년도인가? 첫 년도는 0살이다
print(years_lists[3])

#7.3 years_lists 중 가장 나이가 많을 때는 몇 년도인가?
print(years_lists[-1])

#7.4 "mozzarella", "cinderella", "salmonella" 세 문자열을 요소로 갖는 "things" 리스트를 만들어보자
things=["mozzarella", "cinderella", "salmonella"]

#7.5 things 리스트에서 사람 이름의 첫 글자를 대문자로 바꿔서 출력해보자. 그러면 리스트의 요소가 변경되는가?
things[1]=things[1].capitalize()
print(things)

#7.6 things 리스트의 치즈 요소를 모두 대문자로 바꿔서 출력해보자
things[0]=things[0].upper()
print(things)

#7.7 things 리스트에 질병 요소가 있다면 제거한 뒤 리스트를 출력해보자
things.pop(2)
print(things)

#7.8 "Groucho", "Chico", "Harpo" 세 문자열 요소를 갖는 surprise 리스트를 만들어보자
surprise=["Groucho","Chico","Harpo"]

#7.9 surprise 리스트의 마지막 요소를 소문자로 변경하고, 단어를 뒤집은 다음에 첫 글자를 대문자로 바꿔보자
surprise[-1]=surprise[-1].lower()
surprise[-1]=surprise[-1][-1::-1]
surprise[-1]=surprise[-1].capitalize()
print(surprise)