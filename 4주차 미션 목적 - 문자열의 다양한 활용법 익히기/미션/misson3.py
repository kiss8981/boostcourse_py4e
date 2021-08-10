import re

guest_book = u"""김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

def checkPhoneNumber(phone_number, name):
    phone_number = re.match('^\d{3}-\d{4}-\d{4}$', phone_number)

    if phone_number == None:
        print(f'잘못 쓴 번호입니다. ({name})')  
    else:
        pass


text_save = open("guest_book.txt", "w", encoding='utf-8')
text_save.write(guest_book)
text_save.close()
try:
    fh = open("guest_book.txt","r", encoding='utf-8')
except:
    print("파일을 열지 못했습니다.")
    quit()

for line in fh:
    line = line.rstrip()
    line = line.split(',')
    checkPhoneNumber(line[1], line[0])



