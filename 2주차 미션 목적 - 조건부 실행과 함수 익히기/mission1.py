import random

sel = ['가위', '바위', '보']
result = {0: '컴퓨터가 패배했습니다.', 1: '컴퓨터가 승리했습니다.', 2: '비겼습니다.'}

def check(user, com):

    if not user in sel:
       print('잘못입력하였습니다.')
       return False

    if user == com:
        state = 2
    elif user == '가위' and com == '바위':
        state = 1
    elif user == '바위' and com == '보':
        state = 1
    elif user == '보' and com == '가위':
        state = 1
    else:
        state = 0
    print(f'나: {user} \n컴퓨터: {com} \n{result[state]}')
    return True


while True:
    user = input("가위, 바위, 보 : ")
    com = sel[random.randint(0, 2)]
    if check(user, com):
        break