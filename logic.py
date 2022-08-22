import random

def base_read(letters: int):
    '''
    Принимает количество букв в слове, считывает из файла строку со словами с заданным количеством букв. 
    Возвращает эту строку
    '''
    if letters == 3:
        s = 1
    elif letters == 4:
        s = 2
    else:
        s = 3
    with open('words.txt', 'r', encoding= 'utf-8') as file:
        for item in range(s):
            line = file.readline()
        return line

def change_word(letters: int): 
    '''
    Принимает количество букв в слове, вызывает функцию считывания нужнй строки из файла,
    получает из функции строку со словами с нужным количеством букв.
    Возвращает случайное слово из этой строки.
    '''
    word = base_read(letters).split()
    n = random.randint(0, len(word)-1)
    return word[n]


#print(change_word(3))


def solution(word: str, unknown: str):
    bull = 0
    cow = 0
    for i in range (len(unknown)):
        if word[i] == unknown[i]:
            bull += 1
        elif unknown.find(word[i]) != -1:
            cow +=1
    return (bull, cow)


# unk = change_word(4)
# solution('жаль', unk)