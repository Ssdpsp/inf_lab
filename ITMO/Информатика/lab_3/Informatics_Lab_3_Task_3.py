import re
def f(text, num):
    changed_text = text
    rr= r'\b(\w+?)(?:ая|яя|ое|ее|ую|юю|ой|ей|ый|ий|ой|ые|ие|ого|ими|ом|ем|ым|им|ыми|ых|его|ому|ему|их)\b'
    reg_r = 'ая|яя|ое|ее|ую|юю|ой|ей|ый|ий|ой|ые|ие|ого|ими|ом|ем|ым|им|ыми|ых|его|ому|ему|их'

    words = list(set(re.findall(rr, text))) 

    for i in words:
        if text.count(i)>1: 
            regex_pattern = rf"\b{i}(?:{reg_r})?\b"
            sp = re.findall(regex_pattern, text)
            otv = sp[num-1]
            for d in sp:
                changed_text = changed_text.replace(d, otv)
    return changed_text

text = 'Этот большой и красивый дом стоит на большой красивой поляне. Красивый закат. Маленький пёс на фоне большого дома кажется малышом'
number = 1
print ('Тест №1 \nТекст:',text, '\n')
otv=f(text.lower(), number)
print(otv, '\n')

text2 = 'В большом лесу, по большой тропе, мимо больших деревьев, мы увидели малое озеро с малыми рыбками, и сквозь малое отверстие в кустах пробивался большой луч света.'
number2 = 1
print ('Тест №2 \nТекст:',text2, '\n')
otv2=f(text2.lower(), number2)
print(otv2, '\n')

text3 = ' В тихом уголке, с тихими шорохами тихой природы, мы наблюдали за ярким пламенем яркого костра, отбрасывавшего яркие тени на яркую листву'
number3 = 1
print ('Тест №3 \nТекст:',text3, '\n')
otv3=f(text3.lower(), number3)
print(otv3, '\n')

text4 = 'новый новейшее новому новее нового старина старче старый старого старому наистарейшему старость'
number4 = 2
print ('Тест №4 \nТекст:',text4, '\n')
otv4=f(text4.lower(), number4)
print(otv4, '\n')

text5 = 'Светлый светлому светлого светлой темный темного темному тёмный темнее темнота темнище'
number5 = 3
print ('Тест №5 \nТекст:',text5, '\n')
otv5=f(text5.lower(), number5)
print(otv5, '\n')