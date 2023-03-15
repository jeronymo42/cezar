lowercase_letters_eng = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
uppercase_letters_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' 
def rotation():
    while True:
        try:
            x = input('Введите сдвиг...\n')
            x = int(x)
        except:
            print('Введите сдвиг в числовом формате!\n')
            continue
        return x
def language():
    while True:
        try:
            x = input('Выберите язык (eng / rus)\n')
            if x not in ['eng','rus']:
                raise Exception
        except:
            print('Введите язык в предложенном формате: "eng" или "rus"!\n')
            continue
        return True if x == 'rus' else False
while True:        
    text = input('Введите текст для обработки...\n')
    lang = language()
    rot = rotation()
    newText = ''
    if lang:
        for symb in text:
            if symb.isalpha():
                if symb.islower():
                    newText += lowercase_letters_rus[(lowercase_letters_rus.index(symb) + rot) % len(lowercase_letters_rus)]
                else:
                    newText += uppercase_letters_rus[(uppercase_letters_rus.index(symb) + rot) % len(uppercase_letters_rus)]
            else:
                newText += symb
    else:
        for symb in text:
            if symb.isalpha():
                if symb.islower():
                    newText += lowercase_letters_eng[(lowercase_letters_eng.index(symb) + rot) % len(lowercase_letters_eng)]
                else:
                    newText += uppercase_letters_eng[(uppercase_letters_eng.index(symb) + rot) % len(uppercase_letters_eng)]
            else:
                newText += symb
    print(newText)
        
