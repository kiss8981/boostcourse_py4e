age = int(input("나이를 적어주세요 : "))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
if birth == 0:
    print(f"미국나이는 {age}살 입니다")
if birth == -1:
    print(f"미국나이는 {age - 1}살 입니다")
