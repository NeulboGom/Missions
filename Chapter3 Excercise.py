#Chapter3 Excercise

#3.1
seconds=1
minuite=60*seconds
hour=60*minuite
print(hour)

#3.2 계산한 결과를 seconds_per_hour 변수에 저장해보자
seconds_per_hour=hour
print(seconds_per_hour)
#3.3 1일은 몇 초인가? seconds_per_hour 변수를 사용해보자
day=24*seconds_per_hour
print(day)

#3.4 계산한 결과를 seconds_per_day에 저장해보자
seconds_per_day=day

#3.5 부동소수점(/) 나눗셈을 사용해서 seconds_per_day를 seconds_per_hour로 나누어보자
print(seconds_per_day/seconds_per_hour)

#3.6 정수(//) 나눗셈을 사용해서 seconds_per_day를 seconds_per_hour로 나눈다. 3.5문제 결과에서 본 .0 부분을 제외하고 결과가 같은가?
print(seconds_per_day//seconds_per_hour)