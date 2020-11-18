Voprosi=open('Voprosi.txt','r',encoding=('utf8'))

import random
def get_question():
    with open ('Voprosi.txt','r',encoding='utf-8') as f:
        question_list = f.read().splitlines()
        number_question = random.randrange(0, len(question_list))
        question_answer = str (question_list[number_question])
        for i in range(0, len(question_answer)):
            if question_answer[i]==';':
                question = question_answer[0:i]
                answer = question_answer[i+1:len(question_answer)]
        return answer, question
answer, question = get_question()
print(question)

curent_view = []
for i in range(0,len(answer)):
    curent_view.append('*')
print(''.join(curent_view))

guesses=0
correctLetters = ""

while  guesses != 3:
    user = input ('Введите букву или назовите слово: ').lower()
    if user == answer:
        print('Молодцы!');break
    if user in answer:
        print ('Есть такая буква!')
        correctLetters += user
        guess_part = ""
        for word_letter in answer:
            if word_letter in correctLetters:
                guess_part += word_letter
            else:
                guess_part += "*"
        print("Угаданные буквы: ", guess_part)
    else:
        print('Такой буквы нет!')
        guesses += 1
    if guess_part == answer:
       print('Вы правильно назвали все буквы!');break
       
if guesses==3:
    print('Конец игры!')