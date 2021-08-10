import re

def make_comma(num):
    value = str(num).split('.')
    if len(value) == 2:
        print(re.sub('(?<=\d)(?=(\d{3})+(?!\d))',',', str(value[0])) +'.'+ str(value[1]))
    else:
        print(re.sub('(?<=\d)(?=(\d{3})+(?!\d))',',', str(num)))

while True:
    num = input("숫자를입력하세요:")

    if str(num) == "done":
        break

    try:
        num = int(num)
    except:
        print('숫자만입력가능합니다.')
        continue

    make_comma(num)