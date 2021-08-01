import random

games = int(input("몇 판을 진행하시겠습니까? : "))

def rsp_advanced(games):
    gamesNow = 0
    while True:
        if games == gamesNow:
            break
        my = input("가위, 바위, 보 또는 0, 1, 2를 입력하세요: ")
        try: 
            user = int(my)
        except:
            if my == "가위":
                user = 0
            elif my == "바위":
                user = 1
            elif my == "보":
                user = 2
            else: user = 3
        if user > 2 or user < 0:
            print('가위, 바위, 보 또는 0, 1, 2만 입력하세요')
            gamesNow - 1
            continue
        def show_choice(choice):
            if choice == 0: return "가위"
            elif choice == 1: return "바위"
            elif choice == 2: return "보"
        com = random.randint(0, 2)
        print("나의 선택:", show_choice(user))
        print("컴퓨터의 선택:", show_choice(com))
        if user == com:
            res = 0
        elif user < com:
            if com - user == 2:
                res = 2
            else: res = 1
        elif user > com:
            if user - com == 2:
                res = 1
            else: res = 2
        def show_result(res):
            if res == 0: 
                print("무승부입니다.")
            elif res == 1: 
                print("컴퓨터의 승리입니다.")
            elif res == 2: 
                print("당신의 승리입니다.")
        show_result(res)
        gamesNow = gamesNow + 1



rsp_advanced(games)