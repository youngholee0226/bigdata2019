# coding: cp949
age=int(input("나이를 입력하세요: "))
if age >=0 and age <=3 or age >=66:
    print('요금은 무료입니다.')
elif age >=4 and age <=13 :
    print("요금은 [2000]원입니다.")

elif age >=14 and age <=18 :
    print("요금은 [3000]원입니다.")

elif age >=19 and age <=65 :
    print("요금은 [5000]원입니다.")


