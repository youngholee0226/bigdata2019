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
    cost = "5000"

else:
    grade = "����"
    fee = "����"

if cost == "����":
    print("���ϴ� %s ����̸� ����� %s �Դϴ�." %(grade,fee))
    exit()    

if fee==0:
    fee('���ϴ� %s ����̸�, ����� ���� �Դϴ�.'%grade)
    print('�����մϴ�. Ƽ���� �����մϴ�.')

else:
    print('���ϴ� %s ����̸�, ����� %s �Դϴ�.'%(grade,fee))

coast=int(input('����� �Է��ϼ��� : '))
input_fee=coast-fee

if ('���' in grade or 'û�ҳ�' in grade or '����' in grade) and input_price<0:
    input_fee * -1
    print('%s�� ���ڶ��ϴ�. �Է��Ͻ� %s�� ��ȯ�մϴ�.'%(input_fee,input_fee))

elif ('���' in grade or 'û�ҳ�' in grade or '����' in grade) and input_price>0:
    print('�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s�� ��ȯ�մϴ�.'%input_fee)

else:
    print('�����մϴ�. Ƽ���� �����մϴ�.')
    
