# coding: cp 949

age = int(input"나이를 입력하세요:"))

if age < 0:
    print("다시 입력하세요")
    exit()

elif age >=0 and age <=3:
   grade = "유아"
   fee = "무료"

elif age >=4 and age <= 13:
    grade = "어린이"
    fee = "2000"

elif age >= 14 and age <= 18:
    grade ="청소년"
    fee = "3000"

elif age >= 19 and age <= 65:
    grade = "성인"
    cost = "5000"

else:
    grade = "노인"
    fee = "무료"

if cost == "무료":
    print("귀하는 %s 등급이며 요금은 %s 입니다." %(grade,fee))
    exit()    

if fee==0:
    fee('귀하는 %s 등급이며, 요금은 무료 입니다.'%grade)
    print('감사합니다. 티켓을 발행합니다.')

else:
    print('귀하는 %s 등급이며, 요금은 %s 입니다.'%(grade,fee))

coast=int(input('요금을 입력하세요 : '))
input_fee=coast-fee

if ('어린이' in grade or '청소년' in grade or '성인' in grade) and input_price<0:
    input_fee * -1
    print('%s가 모자랍니다. 입력하신 %s를 반환합니다.'%(input_fee,input_fee))

elif ('어린이' in grade or '청소년' in grade or '성인' in grade) and input_price>0:
    print('감사합니다. 티켓을 발행하고 거스름돈 %s를 반환합니다.'%input_fee)

else:
    print('감사합니다. 티켓을 발행합니다.')
    
