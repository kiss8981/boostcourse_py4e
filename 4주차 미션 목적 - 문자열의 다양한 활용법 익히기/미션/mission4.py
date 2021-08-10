import re

userNumber = input('주민등록 번호를 입력해주세요: ')
check_id = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ')

def checkUserNumber(userNumber, check_id):
    if check_id == 'o':
        checkNumber  = re.match('\d{2}([0]\d|[1][0-2])([0][1-9]|[1-2]\d|[3][0-1])[-]*[3-4]\d{6}', userNumber)
        if checkNumber == None:
            print("잘못된 번호입니다.\n올바른 번호를 넣어주세요")
        else:
            if userNumber[7] == '3':
                print(f'{userNumber[0:2]}년 {userNumber[2:4]}월 남자')
            elif userNumber[7] == '4':
                print(f'{userNumber[0:2]}년 {userNumber[2:4]}월 여자')
    elif check_id == 'x':
        checkNumber  = re.match('\d{2}([0]\d|[1][0-2])([0][1-9]|[1-2]\d|[3][0-1])[-]*[1-2]\d{6}', userNumber)
        if checkNumber == None:
            print("잘못된 번호입니다.\n올바른 번호를 넣어주세요")
        else:
            if userNumber[7] == '1':
                print(f'{userNumber[0:2]}년 {userNumber[2:4]}월 남자')
            elif userNumber[7] == '2':
                print(f'{userNumber[0:2]}년 {userNumber[2:4]}월 여자')
    else:
        print('o 또는 x만 입력해주세요')

checkUserNumber(userNumber, check_id)