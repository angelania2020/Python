schotchik_voprosov=0 #Счётчик вопросов, в начале игры 0
otgadali=0
while schotchik_voprosov<10: #Цикл, играем 10 раз, т.к. 10 вопросов

    def viktorina(): #Задаем функцию для викторины
        with open ('voprosi.txt','r',encoding='utf8') as file:
            spisok_voprosov = file.read().splitlines()
            strochka = spisok_voprosov[schotchik_voprosov]
            vopros_otvet = str(strochka)
            for i in range(0, len(vopros_otvet)):
                if vopros_otvet[i]==';':
                    vopros = vopros_otvet[0:i]
                    otvet = vopros_otvet[i+1:len(vopros_otvet)]
            return otvet, vopros #Функция выдает ответ и вопрос
    
    otvet, vopros = viktorina() #Задаем переменные
    
    print(vopros)
    #Печатаем звездочки для скрытого слова:
    skritoje_slovo = [] 
    for bukva in range(0,len(otvet)):
        skritoje_slovo.append('*')
    print(''.join(skritoje_slovo))

    popitki=0
    otgadannije_bukvi = '' #Сначала нет отгаданных букв

    while  popitki != 3:
        #Пользоатель вводит свою догадку:
        dogadka = input('Введите букву или слово: ').lower()
        if dogadka == 'exit':
            schotchik_voprosov+=10
            break
        if dogadka == otvet:
            print('Молодцы!');print()
            otgadali +=1
            break
        if dogadka in otvet and dogadka not in otgadannije_bukvi:
            print ('Есть такая буква!')
            otgadannije_bukvi += dogadka
            podbor_bukv = '' #Для вывода отгаданных и скрытых букв
            for bukva_otveta in otvet:
                if bukva_otveta in otgadannije_bukvi:
                    podbor_bukv += bukva_otveta
                else:
                    podbor_bukv += "*"
            print("Угаданные буквы: ", podbor_bukv)
        elif dogadka in otgadannije_bukvi:
            print ('Вы уже называли эту букву!')
            popitki += 1
        else:
            print('Такой буквы нет или неверное слово!')
            popitki += 1
        if podbor_bukv == otvet:
            print('Вы правильно назвали все буквы!');print()
            otgadali +=1
            break
     
    if popitki == 3:
        print('Вы не угадали слово! Правильный ответ: {}.'.format(otvet))
        print()
        
    schotchik_voprosov+=1 
            
if schotchik_voprosov==10:
        print('Конец игры! Вы отгадали {} слов(а).'.format(otgadali))