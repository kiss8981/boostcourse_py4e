import random

def bs31():
    num = 0

    while True :
        my = input("My turn - 숫자를 입력하세요 : ")
        my_list = my.split()
        if len(my_list) > 3 :
            print("최대 세 개의 숫자만 입력 가능합니다.")
            continue

        if int(my_list[0]) != num + 1 :
            print(f"{num + 1} 이상인 숫자부터 입력이 가능합니다")
            continue

        elif len(my_list) == 3 :
            if int(my_list[0]) + int(my_list[2]) != int(my_list[1])*2 :
                print("연속된 숫자만 입력 가능합니다.")
                continue

        elif len(my_list) == 2 :
            if int(my_list[1]) - int(my_list[0]) != 1 :
                print("연속된 숫자만 입력 가능합니다.")
                continue

        if str(31) in my_list :
            print("사용자 패배")
            break

        if str(30) in my_list :
            print("사용자 승리")
            break

        num = int(my_list[-1])

        print("현재 숫자 : "+ str(num))

        computer_num = random.randint(1, 3)
        computer_list = []

        for i in range(computer_num) :
            num += 1
            computer_list.append(num)

            print(f"컴퓨터: {num}")

            if num == 30 :
                break

        print(f"현재 숫자 : {str(num)}\n")

        if 30 in computer_list :
            print("사용자 패배")
            break

        if 31 in computer_list :
            print("사용자 승리")
            break

bs31()