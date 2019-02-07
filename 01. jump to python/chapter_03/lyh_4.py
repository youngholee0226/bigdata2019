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
    fee = "5000"

else:
    grade = "노인"
    fee = "무료"

if fee!='무료':
    ifee=int(fee[:4])
    select = int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드)"))

    if select==1:

            sfee = int(input("요금을 입력하세요:"))

            if ifee==sfee:
                print("감사합니다. 티켓을 발행합니다.")
            elif ifee>sfee:
                print("%d원이 모자랍니다. 입력 하신 %d원을 반환합니다."%((ifee-sfee),sfee))
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환 합니다."%(sfee-ifee))

    elif select==2:
         dfee=ifee*0.9
         if age>=60 and age<=65: dfee*=0.95

         print("%d원 결제 되었습니다. 티켓을 발행합니다."%dfee)

else: print("감사합니다. 티켓을 발행합니다.")
    
