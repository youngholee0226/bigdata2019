# coding: cp 949

age = int(input"���̸� �Է��ϼ���:"))

if age < 0:
    print("�ٽ� �Է��ϼ���")
    exit()

elif age >=0 and age <=3:
   grade = "����"
   fee = "����"

elif age >=4 and age <= 13:
    grade = "���"
    fee = "2000"

elif age >= 14 and age <= 18:
    grade ="û�ҳ�"
    fee = "3000"

elif age >= 19 and age <= 65:
    grade = "����"
    fee = "5000"

else:
    grade = "����"
    fee = "����"

if fee!='����':
    ifee=int(fee[:4])
    select = int(input("��� ������ �����ϼ���. (1:����, 2:���� ���� �ſ�ī��)"))

    if select==1:

            sfee = int(input("����� �Է��ϼ���:"))

            if ifee==sfee:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif ifee>sfee:
                print("%d���� ���ڶ��ϴ�. �Է� �Ͻ� %d���� ��ȯ�մϴ�."%((ifee-sfee),sfee))
            else:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ �մϴ�."%(sfee-ifee))

    elif select==2:
         dfee=ifee*0.9
         if age>=60 and age<=65: dfee*=0.95

         print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%dfee)

else: print("�����մϴ�. Ƽ���� �����մϴ�.")
    
