sentence = """
Smooth like butter
Like a criminal undercover
Gon' pop like trouble
Breakin' into your heart like that
Cool shade stunner
...
Get it, let it roll
Get it, let it roll
Get it, let it roll
...
Smooth like (butter)
Cool shade (stunner)
And you know we don't stop
Hot like (summer)
Ain't no (bummer)
You be like oh my god
We gon' make you rock and you say (yeah)
We gon' make you bounce and you say (yeah)
Hotter?
Sweeter!
Cooler?
Butter!
Get it, let it roll
"""

word = input("찾으시는 글자를 입력하세요 : ")

def find(sentence, word):
    text_save = open("week_4_2.txt","w",encoding="UTF-8")
    text_save.write(sentence)
    text_save.close()

    file = open('week_4_2.txt', 'r')
    text_read = file.read()
    print(text_read)

    count = text_read.count(word)
    file.close()
    print(f'{word} 단어의 갯수는 {count}개 입니다!')

find(sentence, word)